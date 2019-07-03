import sys
import os


def main(fileContent, filename):
    global fileExtension
    fileExtension = os.path.splitext(filename)[1]
    print filename
    print fileExtension
    for lines in fileContent:
        print lines
    createFile(filename)

def createFile(filename):
    fileString = filename[-len(str(fileExtension))]
    print len(str(fileExtension))
    lastSlash = 0
    iterator = 0
    while filename[iterator] != "":
        print "1"
        if filename[iterator] == "/":
            lastSlash = iterator
        iterator += 1
    fileString = fileString[lastSlash:end]    
    #fileString = open((str(fileString) + str(fileExtension)), "w+")
    print "here"
