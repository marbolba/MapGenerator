import numpy as np
import matplotlib.pyplot as plt

from tools.pickRandom import PickRandom
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np


class Generator:

    def __init__(self):
        self.settings = self.Settings()

    class Settings:
        def __init__(self):
            self.minVal = 0
            self.maxVal = 5
            self.initialResolution = (5, 5)
            self.incrementNumber = 5

        def set(self, min=1, max=2, resolution=(5, 5), incrementNumber=5):
            self.minVal = min
            self.maxVal = max
            self.initialResolution = resolution
            self.incrementNumber = incrementNumber

    def generate(self):
        terrain = np.random.randint(self.settings.minVal, self.settings.maxVal, self.settings.initialResolution)
        for i in range(self.settings.incrementNumber):
            terrain = self.__increaseRes(terrain)
        self.smoothEfect(terrain)
        self.drawMap(terrain)

    def drawMap(self, constMap):
        plt.matshow(constMap)
        plt.show()

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        X = np.arange(0, 129, 1)
        Y = np.arange(0, 129, 1)
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(X, Y, constMap)

        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    def __increaseRes(self, constMap):
        newMap = np.empty([len(constMap) + len(constMap) - 1, len(constMap[0]) + len(constMap[0]) - 1], )
        newMap[:] = np.nan

        # Fill with known values
        for i in range(len(constMap)):
            for j in range(len(constMap[0])):
                ii = i
                ij = j
                if i != 0:
                    ii = i * 2
                if j != 0:
                    ij = j * 2
                newMap[ii][ij] = constMap[i][j]

        # Fill with new values
        for i in range(len(newMap)):
            for j in range(len(newMap[0])):
                if np.isnan(newMap[i][j]):
                    if i % 2 == 0:
                        newMap[i][j] = PickRandom.rand2(newMap[i][j - 1], newMap[i][j + 1])
                    elif i % 2 == 1:
                        if j % 2 == 0:
                            newMap[i][j] = PickRandom.rand2(newMap[i - 1][j], newMap[i + 1][j])
                        else:
                            # problem z mixem ( od dolu sa NaN-e )
                            newMap[i][j] = PickRandom.rand4(newMap[i - 1][j - 1], newMap[i - 1][j + 1],
                                                            newMap[i + 1][j - 1],
                                                            newMap[i + 1][j + 1])

            # constMap.ass
        return newMap

    def smoothEfect(self, constMap):
        for i in range(len(constMap)):
            for j in range(len(constMap[0])):
                if i != 0 and j != 0 and i != len(constMap) - 1 and j != len(constMap[0]) - 1:
                    if constMap[i - 1][j] == constMap[i + 1][j] and constMap[i][j - 1] == constMap[i][j + 1]:
                        constMap[i][j] = PickRandom.rand2(constMap[i - 1][j], constMap[i][j - 1])
                    elif constMap[i - 1][j] == constMap[i + 1][j]:
                        constMap[i][j] = constMap[i - 1][j]
                    elif constMap[i][j - 1] == constMap[i][j + 1]:
                        constMap[i][j] = constMap[i][j - 1]


if __name__ == '__main__':
    g = Generator()
    g.generate()
