import sys
import os
import time
def main(filename):
    global fileExtension, filepath
    filepath = filename
    fileExtension = os.path.splitext(filename)[1]
    createFile(filename)
    changeFile()
def createFile(filename):
    nFile = open((str(getFilePath()) + ".py"), "w+")
    nFile.close()
def changeFile():
    nFile = open((str(getFilePath()) + ".py"), "a+")
    nFile.write("from chimera import runCommand\r\n")
    nFile.write("cmds = [\r\n")
    f = open(str(getFilePath()) + ".txt", "r")
    for lines in f:
        insLines = ""
        lines = lines.rstrip().replace('\\', '\\\\')
        lines = lines.rstrip().replace('\"', '\\\"')
        insLines = lines
        nextLine = "    \"" + insLines + "\",\r\n"
        nFile.write(nextLine)
    nFile.write("]\r\n")
    nFile.write("for cmd in cmds:\r\n")
    nFile.write("    try:\r\n")
    nFile.write("        runCommand(cmd)\r\n")
    nFile.write("    except:\r\n")
    nFile.write("        pass\r\n")
    nFile.close()
    f.close()
def findWord(word, stringFind):
    index = stringFind.find(word)
    return index
def getFilePath():
    return filepath[:-len(str(fileExtension))]
