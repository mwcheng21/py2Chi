import sys
import os

def main(fileContent, filename):
    global fileExtension, filepath
    filepath = filename
    fileExtension = os.path.splitext(filename)[1]
    print filename
    print fileExtension
    createFile(filename)
    changeFile(fileContent)
def createFile(filename):
    print "creating new file"
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
    print "new file " + str(fileString) + " created"
def changeFile(fileContent):
    iterate = 0
    nFile = open((str(fileString) + ".txt"), "a+")#str(fileExtension)), "a+")
    PrevP = -1
    molNum = 0
    for lines in fileContent:
        nextLine = lines
        #nFile.write(lines + "\r\n")
        ##str(exec 'lines[:4] load(lines)' in globals(), locals())
        if lines[:4] == 'load':
            nextLine = load(lines, molNum)
            molNum += 1
        if lines[:4] == 'hide' or lines[:4] == 'show' or lines[:4] == 'set ':
            nextLine = ''
        if lines[:4] == 'spec':
            nextLine = spec(lines, molNum-1) + "\r\n"
        if lines[:4] == 'colo':
            nextLine = "color #191919 #" + str(molNum-1)  + "\r\n"
        if lines[:4] == 'alig':
            nextLine = split(lines, molNum-1) + "\r\n" + "\r\n"
        if lines[:4] == 'cent':
            nextLine = "center #0" + "\r\n"
        if lines[:4] == 'pair':
            nextLine = pairFit(lines, molNum-1) + "\r\n" + "\r\n"
        nFile.write(nextLine)
        if (iterate*100/len(fileContent)) != PrevP:
            print str(iterate*100/len(fileContent)) + "\% done"
            PrevP = iterate*100/len(fileContent)
        iterate += 1
    print "finished"
def load(strInfo, iterate):
    strInfo1 = strInfo[5:]
    strInfo2 = "open #" +str(iterate) + " pdb:" + strInfo1  + "\r\n"
    return strInfo2
def spec(strInfo, iterate):
    strInfo1 = strInfo[findWord("chain ",strInfo):]
    strInfo2 = "rainbow #" + str(iterate) + ":." + strInfo1[6:7].lower()
    if len(strInfo2) > 1:
        strInfo1 = strInfo[findWord("resi ",strInfo):]
        strInfo3 = strInfo2 + ":" + strInfo1[5:]
        strInfo2 = strInfo3
    return strInfo2
def split(strInfo, iterate):
    strin= "mmaker #0" + align(strInfo[findWord(", ", strInfo)+1:],iterate)
    return strin + " #" + str(iterate) + align(strInfo[:findWord(", ", strInfo)], iterate) + " pair ss iter false"
def align(strInfo, iterate):
    str1 = spec(strInfo, iterate)
    str2 = str1[9+iterate:]
    return str2
def pairFit(strInfo, iterate):
    strin= "match #0" + pFit(strInfo[findWord(", ", strInfo)+1:],iterate)
    return strin + " #" + str(iterate) + pFit(strInfo[:findWord(", ", strInfo)], iterate)
def pFit(strInfo, iterate):
    strChain = strInfo[findWord("//", strInfo)+1:].lower()
    strReturn = ":." + strChain[1:2]
    print strChain
    strRes = strChain[findWord("/", strChain)+1:]
    strRes = strRes[findWord("/", strChain)+2:]
    strReturn = strReturn + ":" + strRes[:findWord("/", strRes)]
    if len(strRes) > 0:
        strMol = strRes[findWord("/", strRes)+1:]
        strReturn = strReturn + "@" + strMol
    return strReturn
def findWord(word, stringFind):
    index = stringFind.find(word)
    return index
##def getFilePath():0
##    print filepath[:-len(str(fileExtension))] +".txt"
##    return filepath[:-len(str(fileExtension))] +".txt"
