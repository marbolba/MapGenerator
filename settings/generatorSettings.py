import numpy as np
from tools.inputNumber import inputNumber

class GeneratorSettings:
    manualSeed = False
    normalDistribution = True

    # manual settings
    terrainSeed = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [5, 3, 4, 3, 5, 4, 2, 1, 1, 1],
        [8, 8, 9, 7, 8, 7, 6, 1, 1, 1],
        [1, 1, 1, 1, 1, 5, 7, 1, 1, 1],
        [1, 1, 1, 1, 1, 4, 6, 1, 1, 1],
        [1, 1, 1, 4, 6, 8, 5, 1, 1, 1],
        [1, 1, 1, 1, 5, 5, 4, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    startPoint = [0,0]
    endPoint = [0,0]

    # auto settings
    # terrain
    minVal = 0
    maxVal = 10
    initialResolution = (5, 5)
    incrementNumber = 5

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
        return [GeneratorSettings.startPoint,GeneratorSettings.endPoint]
                
    @staticmethod
    def setWaypoints():
        x1 = inputNumber("Enter startPoint X : ")
        y1 = inputNumber("Enter startPoint Y : ")
        x2 = inputNumber("Enter endPoint X : ")
        y2 = inputNumber("Enter endPoint Y : ")
        GeneratorSettings.startPoint = [x1,y1]
        GeneratorSettings.endPoint = [x2,y2]