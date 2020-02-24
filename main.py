from datetime import datetime

from terrainGenerator.generator import Generator

if __name__ == '__main__':
    # generate foler name
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y_%H%M%S")
    file = "plots/{}/".format(timestampStr)

    g = Generator()
    g.outputFolder(file)
    g.probeName('terrainLabel')
    g.generate()
    g.saveToFile()