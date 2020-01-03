import numpy as np
import matplotlib.pyplot as plt

from tools.pickRandom import PickRandom
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# TODO add region avg height report
class Generator:

    def __init__(self):
        self.settings = self.Settings()
        self.terrain = []

    class Settings:
        def __init__(self):
            self.minVal = 0
            self.maxVal = 10
            self.initialResolution = (3, 5)
            self.incrementNumber = 5

        def set(self, min=1, max=2, resolution=(5, 5), incrementNumber=5):
            self.minVal = min
            self.maxVal = max
            self.initialResolution = resolution
            self.incrementNumber = incrementNumber

    def generate(self):
        self.__generateInitialTerrain()
        self.__increaseResolution()
        self.__smoothSharpEdges()
        self.__smoothAltitude(4, 3, 0.3)
        self.drawSurf()
        self.drawMap()

    def drawMap(self):
        plt.matshow(self.terrain)
        plt.colorbar()
        plt.show()

    def drawSurf(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        X = np.arange(0, len(self.terrain[0]), 1)
        Y = np.arange(0, len(self.terrain), 1)
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(X, Y, self.terrain, cmap='rainbow', linewidth=0, antialiased=True)
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    def __generateInitialTerrain(self):
        # self.terrain = np.random.randint(self.settings.minVal, self.settings.maxVal, self.settings.initialResolution)
        self.terrain = [[3, 2, 1, 9, 4, 3, 2, 8],
                        [2, 5, 3, 7, 2, 6, 4, 9],
                        [7, 9, 5, 3, 2, 8, 6, 1]]

    def __increaseResolution(self):
        for i in range(self.settings.incrementNumber):
            self.__incrementResolution()
        print("Final terrain resolution:", (len(self.terrain), len(self.terrain[0])))

    def __incrementResolution(self):
        newMap = np.empty([len(self.terrain) + len(self.terrain) - 1, len(self.terrain[0]) + len(self.terrain[0]) - 1])
        newMap[:] = np.nan

        # Fill with known values
        for i in range(len(self.terrain)):
            for j in range(len(self.terrain[0])):
                ii = i
                ij = j
                if i != 0:
                    ii = i * 2
                if j != 0:
                    ij = j * 2
                newMap[ii][ij] = self.terrain[i][j]

        # Fill with new values
        for i in range(len(newMap)):
            for j in range(len(newMap[0])):
                if np.isnan(newMap[i][j]):
                    if i % 2 == 0:
                        newMap[i][j] = PickRandom.rand(newMap[i][j - 1], newMap[i][j + 1],
                                                       (newMap[i][j - 1] + newMap[i][j + 1]) / 2)
                    elif i % 2 == 1:
                        if j % 2 == 0:
                            newMap[i][j] = PickRandom.rand(newMap[i - 1][j], newMap[i + 1][j],
                                                           (newMap[i - 1][j] + newMap[i + 1][j]) / 2)

        # fill middles
        for i in range(len(newMap)):
            for j in range(len(newMap[0])):
                if np.isnan(newMap[i][j]):
                    newMap[i][j] = PickRandom.rand(newMap[i - 1][j], newMap[i + 1][j], newMap[i][j - 1], newMap[i][j + 1])
        self.terrain = newMap

    # smooths surface to remove sharp terrain changes
    def __smoothSharpEdges(self):
        for i in range(len(self.terrain)):
            for j in range(len(self.terrain[0])):
                if i != 0 and j != 0 and i != len(self.terrain) - 1 and j != len(self.terrain[0]) - 1:
                    if self.terrain[i - 1][j] == self.terrain[i + 1][j] and self.terrain[i][j - 1] == self.terrain[i][j + 1]:
                        self.terrain[i][j] = PickRandom.rand2(self.terrain[i - 1][j], self.terrain[i][j - 1])
                    elif self.terrain[i - 1][j] == self.terrain[i + 1][j]:
                        self.terrain[i][j] = self.terrain[i - 1][j]
                    elif self.terrain[i][j - 1] == self.terrain[i][j + 1]:
                        self.terrain[i][j] = self.terrain[i][j - 1]

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
            print('Cannot perform smooth altitude operation')
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
                biggerIndexes = np.argwhere(self.terrain[yStart:yEnd, xStart:xEnd] > regionMean)
                lesserIndexes = np.argwhere(self.terrain[yStart:yEnd, xStart:xEnd] < regionMean)

                # calculate new values
                maxIncrement = smoothRatio * regionMean
                for b in range(len(biggerIndexes)):
                    yIdx = biggerIndexes[b][0] + yStart
                    xIdx = biggerIndexes[b][1] + xStart
                    if self.terrain[yIdx, xIdx] - regionMean > maxIncrement:
                        # max increment
                        self.terrain[yIdx, xIdx] = self.terrain[yIdx, xIdx] - maxIncrement
                    else:
                        # half of remaining increment
                        self.terrain[yIdx, xIdx] = self.terrain[yIdx, xIdx] - (self.terrain[yIdx, xIdx] - regionMean) / 2

                for b in range(len(lesserIndexes)):
                    yIdx = lesserIndexes[b][0] + yStart
                    xIdx = lesserIndexes[b][1] + xStart
                    if self.terrain[yIdx, xIdx] + maxIncrement < regionMean:
                        # max increment
                        self.terrain[yIdx, xIdx] = self.terrain[yIdx, xIdx] + maxIncrement
                    else:
                        # half of remaining increment
                        self.terrain[yIdx, xIdx] = self.terrain[yIdx, xIdx] + (regionMean - self.terrain[yIdx, xIdx]) / 2

    def __saveToFile(self, fileName):
        np.save(fileName, self.terrain)

    def __readFromFile(self, fileName):
        return np.load(fileName)


if __name__ == '__main__':
    g = Generator()
    g.generate()
