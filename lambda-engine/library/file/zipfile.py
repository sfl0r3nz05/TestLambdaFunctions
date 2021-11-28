from zipfile import ZipFile
from os.path import basename

def computeZip(pathFile):
    with ZipFile('./input/function.zip', 'w') as zip:
        zip.write(pathFile, basename(pathFile))
        nPathFile = './input/function.zip'
        return nPathFile
