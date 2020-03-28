from terrainGenerator.generator import Generator
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer

if __name__ == "__main__":
    g = Generator()
    g.generate()

    # save results to file
    resultTerrain = g.getTerrain()
    resultAccessibility = g.getAccessibility()

    FileHandler.saveToFile(resultTerrain,"terrain")
    FileHandler.saveTerrain2D(resultTerrain,"terrain")
    FileHandler.saveTerrain3D(resultTerrain,"terrain")

    FileHandler.saveToFile(resultAccessibility,"accessibility")
    FileHandler.saveTerrain2D(resultAccessibility,"accessibility")
    FileHandler.saveTerrain3D(resultAccessibility,"accessibility")
    
    TerrainDrawer.drawTerrain3D(resultTerrain)
    TerrainDrawer.drawTerrain3D(resultAccessibility)
