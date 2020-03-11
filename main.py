from terrainGenerator.generator import Generator
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer

if __name__ == '__main__':
    g = Generator()
    g.generate()

    # save results to file
    resultTerrain = g.getResult()
    FileHandler.saveToFile(resultTerrain)
    FileHandler.saveTerrain2D(resultTerrain)
    FileHandler.saveTerrain3D(resultTerrain)
    TerrainDrawer.drawTerrain3D(resultTerrain)
