import numpy as np


class GeneratorSettings:
    manualSeed = False

    # manual settings
    terrainSeed = [ [2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2], 
                    [8, 8, 8, 8, 2, 2], 
                    [6, 2, 2, 2, 2, 6], 
                    [6, 2, 8, 8, 8, 8], 
                    [6, 2, 2, 2, 2, 6], 
                    [6, 8, 8, 8, 1, 6], 
                    [6, 6, 6, 2, 2, 2]]

    accessibilitySeed =  [ [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1], 
                    [0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0], 
                    [1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1]]


    # auto settings
    # terrain
    minVal = 0
    maxVal = 5
    initialResolution = (5, 5)
    incrementNumber = 5

    # accessibility
    minAccessVal = 0
    maxAccessVal = 2

    @staticmethod
    def getTerrainSeed():
        if GeneratorSettings.manualSeed:
            return GeneratorSettings.terrainSeed
        else:
            return np.random.randint(GeneratorSettings.minVal,GeneratorSettings.maxVal+1,GeneratorSettings.initialResolution)

    def getAccessibilitySeed():
        if GeneratorSettings.manualSeed:
            return GeneratorSettings.accessibilitySeed
        else:
            return np.random.randint(GeneratorSettings.minAccessVal,GeneratorSettings.maxAccessVal+1,GeneratorSettings.initialResolution)