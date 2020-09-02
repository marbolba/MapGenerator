from terrainGenerator.generator import Generator
from accessibilityGenerator.accessibilityGenerator import AccessibilityGenerator
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer
from settings.generatorSettings import GeneratorSettings
import numpy as np


def runGenerator():
    g = Generator()
    g.generate()

    # save results to file
    resultTerrain = g.getTerrain()

    # TerrainDrawer.drawTerrain2D(resultTerrain)
    TerrainDrawer.drawTerrain3D(resultTerrain)
    # GeneratorSettings.setWaypoints()

    FileHandler.saveToFile(
        resultTerrain, GeneratorSettings.getWaypoints(), name="terrain"
    )
    FileHandler.saveTerrain2D(
        resultTerrain, GeneratorSettings.getWaypoints(), name="terrain"
    )
    FileHandler.saveTerrain3D(resultTerrain, name="terrain")


def showMap(case):
    terrain = FileHandler.readFromFile(f"plots/{case}/terrain.npy")
    TerrainDrawer.getPlot2D(terrain)
    TerrainDrawer.drawTerrain3D(terrain)


def runAccessibilityGenerator():
    g = AccessibilityGenerator(size=(129, 129))
    g.addLine(
        ybounds=(37, 78),
        lineValue=0.3,
        xformula=lambda x: -1.64 * x + 192.8,
        yformula=lambda y: 1 / (-1.64) * (y - 192.8),
        xwidth=10,
    )
    g.generateAccessibility()


if __name__ == "__main__":
    # showMap("24-cze-2020_163110")
    runGenerator()
    # runAccessibilityGenerator()
