from terrainGenerator.generator import Generator
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

def generateAccessibility():
    size = (225,129)
    resultAccessibility = []
    #line
    xbounds = (125,190)
    ywidth = 10
    lineValue = 0.3
    formula = lambda x: 0.3076923076923077*x+1.5384615384615385
    
    # fill with ones
    for y in range(size[1]):    # y
        row = []
        for x in range(size[0]):# x
            row.append(1)
        resultAccessibility.append(row)

    #draw line
    for x in range(xbounds[0],xbounds[1]):
        for y in range(ywidth):   
            resultAccessibility[int(formula(x))+y][x] = lineValue
            

    FileHandler.saveToFile(resultAccessibility, "accessibility")
    FileHandler.saveTerrain2D(resultAccessibility, "accessibility")


if __name__ == "__main__":
    # showMap("case3")
    runGenerator()
