import numpy as np
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer


class AccessibilityGenerator:
    def __init__(self, size):
        self.size = size
        self.resultAccessibility = np.ones((size[1], size[0]))

    def addLine(
        self, lineValue, xformula, yformula, xbounds=0, ybounds=0, ywidth=0, xwidth=0
    ):
        if xbounds != 0:
            for x in range(xbounds[0], xbounds[1]):
                if ywidth != 0:
                    for yw in range(ywidth):
                        self.resultAccessibility[int(xformula(x)) + yw][x] = lineValue
                if xwidth != 0:
                    for xw in range(xwidth):
                        self.resultAccessibility[int(xformula(x))][x + xw] = lineValue
        elif ybounds != 0:
            for y in range(ybounds[0], ybounds[1]):
                if ywidth != 0:
                    for yw in range(ywidth):
                        self.resultAccessibility[y + yw][int(yformula(y))] = lineValue
                if xwidth != 0:
                    for xw in range(xwidth):
                        self.resultAccessibility[y][int(yformula(y)) + xw] = lineValue

    def generateAccessibility(self):
        FileHandler.saveToFile(self.resultAccessibility, name="accessibility")
        FileHandler.saveTerrain2D(self.resultAccessibility, name="accessibility")
        TerrainDrawer.getPlot2D(self.resultAccessibility)
