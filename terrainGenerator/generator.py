import numpy as np

from tools.pickRandom import PickRandom
from settings.generatorSettings import GeneratorSettings


# TODO add region avg height report
class Generator:
    def __init__(self):
        self.terrain = []
        self.terrainAccessibility = []

    def generate(self):
        self.__generateInitialTerrain()
        self.terrain = self.__increaseResolution(self.terrain)
        self.terrain = self.__smoothSharpEdges(self.terrain)
        self.__smoothAltitude(4, 3, 0.3)
        print("Final terrain resolution:", (len(self.terrain), len(self.terrain[0])))

        # generate accessibility mesh
        self.__generateAccessibilityMesh()
        self.terrainAccessibility = self.__increaseResolution(self.terrainAccessibility)
        self.terrainAccessibility = self.__smoothSharpEdges(self.terrainAccessibility)
        print("Final mesh resolution:", (len(self.terrainAccessibility), len(self.terrainAccessibility[0])))

    def getTerrain(self):
        return self.terrain

    def getAccessibility(self):
        return self.terrainAccessibility

    def __generateInitialTerrain(self):
        self.terrain = GeneratorSettings.getTerrainSeed()

    def __generateAccessibilityMesh(self):
        self.terrainAccessibility = GeneratorSettings.getAccessibilitySeed()

    def __increaseResolution(self,terrain):
        for i in range(GeneratorSettings.incrementNumber):
            terrain = self.__incrementResolution(terrain)
        return terrain

    def __incrementResolution(self,terrain):
        newMap = np.empty(
            [
                len(terrain) + len(terrain) - 1,
                len(terrain[0]) + len(terrain[0]) - 1,
            ]
        )
        newMap[:] = np.nan

        # Fill with known values
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                ii = i
                ij = j
                if i != 0:
                    ii = i * 2
                if j != 0:
                    ij = j * 2
                newMap[ii][ij] = terrain[i][j]

        # Fill with new values
        for i in range(len(newMap)):
            for j in range(len(newMap[0])):
                if np.isnan(newMap[i][j]):
                    if i % 2 == 0:
                        newMap[i][j] = PickRandom.rand(
                            newMap[i][j - 1],
                            newMap[i][j + 1],
                            (newMap[i][j - 1] + newMap[i][j + 1]) / 2,
                        )
                    elif i % 2 == 1:
                        if j % 2 == 0:
                            newMap[i][j] = PickRandom.rand(
                                newMap[i - 1][j],
                                newMap[i + 1][j],
                                (newMap[i - 1][j] + newMap[i + 1][j]) / 2,
                            )

        # fill middles
        for i in range(len(newMap)):
            for j in range(len(newMap[0])):
                if np.isnan(newMap[i][j]):
                    newMap[i][j] = PickRandom.rand(
                        newMap[i - 1][j],
                        newMap[i + 1][j],
                        newMap[i][j - 1],
                        newMap[i][j + 1],
                    )
        return newMap

    # smooths surface to remove sharp terrain changes
    def __smoothSharpEdges(self,terrain):
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                if (
                    i != 0
                    and j != 0
                    and i != len(terrain) - 1
                    and j != len(terrain[0]) - 1
                ):
                    if (
                        terrain[i - 1][j] == terrain[i + 1][j]
                        and terrain[i][j - 1] == terrain[i][j + 1]
                    ):
                        terrain[i][j] = PickRandom.rand2(
                            terrain[i - 1][j], terrain[i][j - 1]
                        )
                    elif terrain[i - 1][j] == terrain[i + 1][j]:
                        terrain[i][j] = terrain[i - 1][j]
                    elif terrain[i][j - 1] == terrain[i][j + 1]:
                        terrain[i][j] = terrain[i][j - 1]
        return terrain

    # smooth to avenage terrain changes
    def __smoothAltitude(self, smoothSize=4, smoothStep=2, smoothRatio=0.25):
        # parameters

        # helper constants
        yMax = len(self.terrain)
        xMax = len(self.terrain[0])
        smoothsNumberX = np.math.floor((xMax - smoothSize) / smoothStep + 1)
        smoothsNumberY = np.math.floor((yMax - smoothSize) / smoothStep + 1)

        # guardian block
        if smoothsNumberX < 1 or smoothsNumberY < 1:
            print("Cannot perform smooth altitude operation")
            return

        for i in range(smoothsNumberY):
            for j in range(smoothsNumberX):
                # smooth boundaries
                xStart = j * smoothStep
                yStart = i * smoothStep
                xEnd = j * smoothStep + smoothSize
                yEnd = i * smoothStep + smoothSize
                # print(self.terrain[yStart:yEnd, xStart:xEnd])

                # calc region avg
                regionMean = self.terrain[yStart:yEnd, xStart:xEnd].mean()
                # print('region mean:', regionMean,' reduct:',smoothRatio*regionMean)

                # find bigger / lesser indexes
                biggerIndexes = np.argwhere(
                    self.terrain[yStart:yEnd, xStart:xEnd] > regionMean
                )
                lesserIndexes = np.argwhere(
                    self.terrain[yStart:yEnd, xStart:xEnd] < regionMean
                )

                # calculate new values
                maxIncrement = smoothRatio * regionMean
                for b in range(len(biggerIndexes)):
                    yIdx = biggerIndexes[b][0] + yStart
                    xIdx = biggerIndexes[b][1] + xStart
                    if self.terrain[yIdx, xIdx] - regionMean > maxIncrement:
                        # max increment
                        self.terrain[yIdx, xIdx] = (
                            self.terrain[yIdx, xIdx] - maxIncrement
                        )
                    else:
                        # half of remaining increment
                        self.terrain[yIdx, xIdx] = (
                            self.terrain[yIdx, xIdx]
                            - (self.terrain[yIdx, xIdx] - regionMean) / 2
                        )

                for b in range(len(lesserIndexes)):
                    yIdx = lesserIndexes[b][0] + yStart
                    xIdx = lesserIndexes[b][1] + xStart
                    if self.terrain[yIdx, xIdx] + maxIncrement < regionMean:
                        # max increment
                        self.terrain[yIdx, xIdx] = (
                            self.terrain[yIdx, xIdx] + maxIncrement
                        )
                    else:
                        # half of remaining increment
                        self.terrain[yIdx, xIdx] = (
                            self.terrain[yIdx, xIdx]
                            + (regionMean - self.terrain[yIdx, xIdx]) / 2
                        )
