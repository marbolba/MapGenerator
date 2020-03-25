import numpy as np


class GeneratorSettings:
    manualSeed = False

    # manual settings
    manualSeedArray = [ [2, 2, 2, 2, 2, 2],
                        [2, 2, 2, 2, 2, 2], 
                        [8, 8, 8, 8, 2, 2], 
                        [6, 2, 2, 2, 2, 6], 
                        [6, 2, 8, 8, 8, 8], 
                        [6, 2, 2, 2, 2, 6], 
                        [6, 8, 8, 8, 1, 6], 
                        [6, 6, 6, 2, 2, 2]]


    # auto settings
    minVal = 0
    maxVal = 5
    initialResolution = (4, 8)
    incrementNumber = 5

    @staticmethod
    def getSeedArray():
        if GeneratorSettings.manualSeed:
            return GeneratorSettings.manualSeedArray
        else:
            return np.random.randint(GeneratorSettings.minVal,GeneratorSettings.maxVal,GeneratorSettings.initialResolution
            )
