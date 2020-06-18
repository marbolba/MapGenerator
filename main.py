from terrainGenerator.generator import Generator
from accessibilityGenerator.accessibilityGenerator import AccessibilityGenerator
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer


def runGenerator():
    g = Generator()
    g.generate()

    # save results to file
    resultTerrain = g.getTerrain()

    FileHandler.saveToFile(resultTerrain, "terrain")
    FileHandler.saveTerrain2D(resultTerrain, "terrain")
    FileHandler.saveTerrain3D(resultTerrain, "terrain")

    TerrainDrawer.drawTerrain3D(resultTerrain)
    TerrainDrawer.drawTerrain3D(resultTerrain)


def showMap(case):
    terrain = FileHandler.readFromFile(f"plots/{case}/terrain.npy")
    TerrainDrawer.drawTerrain2D(terrain)
    TerrainDrawer.drawTerrain3D(terrain)

def runAccessibilityGenerator():
    g = AccessibilityGenerator(size=(225,129))
    g.addLine(xbounds = (125,190),ywidth = 10,lineValue = 0.3,formula = lambda x: 0.3076923076923077*x+1.5384615384615385)
    g.generateAccessibility()
    
if __name__ == "__main__":
    # showMap("case3")
    # runGenerator()
    runAccessibilityGenerator()
