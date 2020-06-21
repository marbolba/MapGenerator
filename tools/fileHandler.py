import os
import numpy as np
from datetime import datetime

from tools.terrainDrawer import TerrainDrawer


class FileHandler:
    # generate folder name
    folderPath = "plots/{}/".format(datetime.now().strftime("%d-%b-%Y_%H%M%S"))
    defaultName = "terrain"

    @staticmethod
    def saveToFile(terrain: [] = [], waypoints: [] = [], name=defaultName):
        FileHandler.checkIfFolderExists()
        np.save("{}{}".format(FileHandler.folderPath, name), terrain)
        terrainSize = (len(terrain), len(terrain[0]))
        np.save("{}{}-size".format(FileHandler.folderPath, name), terrainSize)
        if len(waypoints) != 0:
            np.save("{}{}-waypoints".format(FileHandler.folderPath, name), waypoints)

    @staticmethod
    def checkIfFolderExists():
        if not (os.path.exists(FileHandler.folderPath)):
            # create the directory you want to save to
            os.mkdir(FileHandler.folderPath)

    @staticmethod
    def saveTerrain2D(terrain, waypoints: [] = [], name=defaultName):
        plt = TerrainDrawer.drawTerrain2D(terrain, waypoints)
        FileHandler.checkIfFolderExists()
        plt.savefig("{}{}-2d.png".format(FileHandler.folderPath, name))
        plt.close()

    @staticmethod
    def saveTerrain3D(terrain, name=defaultName):
        plt = TerrainDrawer.getPlot3D(terrain)
        FileHandler.checkIfFolderExists()
        plt.savefig("{}{}-3d.png".format(FileHandler.folderPath, name))
        plt.close()

    @staticmethod
    def readFromFile(fileName):
        return np.load(fileName)
