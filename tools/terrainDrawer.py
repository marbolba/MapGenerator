import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

class TerrainDrawer:

    @staticmethod
    def getPlot2D(terrain:[]):
        plt.matshow(terrain)
        plt.colorbar()
        return plt
    
    @staticmethod
    def drawTerrain2D(terrain:[]):
        plt.matshow(terrain)
        plt.colorbar()
        plt.show()

    @staticmethod
    def getPlot3D(terrain:[]):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        X = np.arange(0, len(terrain[0]), 1)
        Y = np.arange(0, len(terrain), 1)
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(X, Y, terrain, cmap='rainbow', linewidth=0, antialiased=True)
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        return plt

    @staticmethod
    def drawTerrain3D(terrain:[]):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        X = np.arange(0, len(terrain[0]), 1)
        Y = np.arange(0, len(terrain), 1)
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(X, Y, terrain, cmap='rainbow', linewidth=0, antialiased=True)
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
    