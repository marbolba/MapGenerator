from terrainGenerator.generator import Generator
from accessibilityGenerator.accessibilityGenerator import AccessibilityGenerator
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer
from settings.generatorSettings import GeneratorSettings


def runGenerator():
    g = Generator()
    g.generate()

    # save results to file
    resultTerrain = g.getTerrain()
    
    TerrainDrawer.drawTerrain3D(resultTerrain)
    GeneratorSettings.setWaypoints()

    FileHandler.saveToFile(resultTerrain, GeneratorSettings.getWaypoints(), name="terrain")
    FileHandler.saveTerrain2D(resultTerrain,GeneratorSettings.getWaypoints(), name="terrain")
    FileHandler.saveTerrain3D(resultTerrain, name="terrain")


def showMap(case):
    terrain = FileHandler.readFromFile(f"plots/{case}/terrain.npy")
    TerrainDrawer.drawTerrain2D(terrain)
    TerrainDrawer.drawTerrain3D(terrain)

def runAccessibilityGenerator():
    g = AccessibilityGenerator(size=(225,129))
    g.addLine(xbounds = (125,190),ywidth = 10,lineValue = 0.3,formula = lambda x: 0.3076923076923077*x+1.5384615384615385)
    g.addLine(xbounds = (20,50),ywidth = 10,lineValue = 0.3,formula = lambda x: 40)
    g.generateAccessibility()
    
if __name__ == "__main__":
    # showMap("case3")
    runGenerator()
    # runAccessibilityGenerator()
