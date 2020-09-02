import numpy as np
from tools.inputNumber import inputNumber


class GeneratorSettings:

    manualSeed = True

    # general settings
    incrementNumber = 5
    startPoint = [0, 0]
    endPoint = [0, 0]

    # manual settings
    terrainSeed = [
        [1, 2, 5, 6, 3, 1],
        [1, 2, 5, 6, 3, 1],
        [1, 2, 4, 6, 3, 1],
        [1, 1, 4, 6, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    # auto settings
    # terrain
    minVal = 1
    maxVal = 3
    initialResolution = (2, 9)
    normalDistribution = False

    @staticmethod
    def getTerrainSeed():
        if GeneratorSettings.manualSeed:
            return GeneratorSettings.terrainSeed
        else:
            if GeneratorSettings.normalDistribution:
                return abs(
                    np.random.normal(
                        GeneratorSettings.minVal,
                        GeneratorSettings.maxVal / 1.5,
                        GeneratorSettings.initialResolution,
                    )
                )
            else:
                return np.random.randint(
                    GeneratorSettings.minVal,
                    GeneratorSettings.maxVal + 1,
                    GeneratorSettings.initialResolution,
                )

    @staticmethod
    def getWaypoints():
        return [GeneratorSettings.startPoint, GeneratorSettings.endPoint]

    @staticmethod
    def setWaypoints():
        x1 = inputNumber("Enter startPoint X : ")
        y1 = inputNumber("Enter startPoint Y : ")
        x2 = inputNumber("Enter endPoint X : ")
        y2 = inputNumber("Enter endPoint Y : ")
        GeneratorSettings.startPoint = [x1, y1]
        GeneratorSettings.endPoint = [x2, y2]
