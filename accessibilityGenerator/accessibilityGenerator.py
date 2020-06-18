import numpy as np
from tools.fileHandler import FileHandler
from tools.terrainDrawer import TerrainDrawer

class AccessibilityGenerator:
    def __init__(self, size):
        self.size = size
        self.resultAccessibility = np.ones((size[1],size[0]))

    def addLine(self, xbounds,ywidth,lineValue,formula):
        for x in range(xbounds[0],xbounds[1]):
            for y in range(ywidth):   
                self.resultAccessibility[int(formula(x))+y][x] = lineValue

    def generateAccessibility(self):
        FileHandler.saveToFile(self.resultAccessibility, "accessibility")
        FileHandler.saveTerrain2D(self.resultAccessibility, "accessibility")
        TerrainDrawer.drawTerrain2D(self.resultAccessibility)