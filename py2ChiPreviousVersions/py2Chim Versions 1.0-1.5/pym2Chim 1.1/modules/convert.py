import sys
import os


def main(fileContent, filename):
    global fileExtension
    fileExtension = os.path.splitext(filename)[1]
    print filename
    print fileExtension
    createFile(filename)
    changeFile(fileContent)
def createFile(filename):
    global fileString
    fileString = filename[:-len(str(fileExtension))]
    lastSlash = 0
    iterator = 0
    for char in str(filename):
        if filename[iterator] == "/":
            lastSlash = iterator
        iterator += 1
    fileString = fileString[(lastSlash+1):]    
    #creates file with same name and extension
    nFile = open((str(fileString) + ".txt"), "w+") #str(fileExtension)), "w+")
    nFile.close()
    
    print str(fileString)
def changeFile(fileContent):
    nFile = open((str(fileString) + ".txt"), "a+")#str(fileExtension)), "a+")
    for lines in fileContent:
        nFile.write(lines + "\r\n")
