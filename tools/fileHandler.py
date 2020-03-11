import os
import numpy as np
from datetime import datetime

from tools.terrainDrawer import TerrainDrawer

class FileHandler:
    # generate folder name
    folderPath = "plots/{}/".format(datetime.now().strftime("%d-%b-%Y_%H%M%S"))
    defaultName = "terrain"

    @staticmethod
    def saveToFile(terrain: []):
        FileHandler.checkIfFolderExists()
        np.save("{}{}".format(FileHandler.folderPath, FileHandler.defaultName), terrain)
        terrainSize = (len(terrain), len(terrain[0]))
        np.save("{}size".format(FileHandler.folderPath), terrainSize)
    
    @staticmethod
    def checkIfFolderExists():
        if not (os.path.exists(FileHandler.folderPath)):
            # create the directory you want to save to
            os.mkdir(FileHandler.folderPath)

    @staticmethod
    def saveTerrain2D(terrain):
        plt = TerrainDrawer.getPlot2D(terrain)
        FileHandler.checkIfFolderExists()
        plt.savefig("{}{}-2d.png".format(FileHandler.folderPath, FileHandler.defaultName))


    @staticmethod
    def saveTerrain3D(terrain):
        plt = TerrainDrawer.getPlot3D(terrain)
        FileHandler.checkIfFolderExists()
        plt.savefig("{}{}-3d.png".format(FileHandler.folderPath, FileHandler.defaultName))