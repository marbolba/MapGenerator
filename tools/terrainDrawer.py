import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


class TerrainDrawer:
    @staticmethod
    def drawTerrain2D(terrain: [], wayPoints: [] = []):
        plt.matshow(terrain)
        if len(wayPoints) != 0:
            plt.plot(wayPoints[0][0], wayPoints[0][1], "o", color="green")
            plt.plot(wayPoints[1][0], wayPoints[1][1], "o", color="red")
        cbar = plt.colorbar()
        cbar.set_label("Z")
        plt.xlabel("X")
        plt.ylabel("Y")
        return plt

    @staticmethod
    def getPlot3D(terrain: []):
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        X = np.arange(0, len(terrain[0]), 1)
        Y = np.arange(0, len(terrain), 1)
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(
            X, Y, terrain, cmap="rainbow", linewidth=0, antialiased=True
        )
        plt.xlabel("X")
        plt.ylabel("Y")
        # plt.zlabel("Z")
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        return plt

    @staticmethod
    def drawTerrain3D(terrain: []):
        plt = TerrainDrawer.getPlot3D(terrain)
        plt.show()
