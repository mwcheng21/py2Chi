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
    global molList
    molList = []
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
            molList.append(lines[5:findWord(".", lines)])
            molNum += 1
        if lines[:4] == 'set ':
            nextLine = ''
        if lines[:4] == 'hide':
            nextLine = hide(lines, molNum-1)
        if lines[:4] == 'show':
            nextLine = show(lines, molNum-1)
        if lines[:4] == 'spec':
            nextLine = spec(lines, molNum-1) + "\r\n"
        if lines[:4] == 'colo':
            nextLine = color(lines, molNum-1) + "\r\n"
        if lines[:4] == 'alig':
            nextLine = split(lines, molNum-1) + "\r\n" + "\r\n"
        if lines[:4] == 'cent':
            nextLine = "center #0" + "\r\n"
        if lines[:4] == 'pair':
            nextLine = pairFit(lines, molNum-1) + "\r\n" + "\r\n"
        if lines[:4] == 'sele':
            nextLine = sele(lines, molNum-1)
        if lines[:8] == 'util.cnc':
            nextLine = "color byhet "+ lines[findWord(" ", lines)+1:] + "\r\n"
        if lines[:8] == 'util.cba':
            nextLine = "color byatom "+ lines[findWord(" ", lines)+1:] + "\r\n" 
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
def hide(strInfo, iterate):
    retLine = ''
    saveit = iterate
    if findWord("chain", strInfo) > 0:
        if findWord("lines", strInfo) >0 :
            retLine = "~ribbon #" + str(iterate) + "\r\n"
            retLine = retLine + "~display #" + str(iterate) + "\r\n"
        if findWord("cartoon", strInfo) >0:
            atomSpec = spec(strInfo, -1)
            retLine = "~ribbon #" + str(iterate) + "\r\n"
            retLine = retLine + "~display #" + str(iterate) + "\r\n"
            #atomSpec = atomSpec[9+len(str(saveit)):]
            retLine = retLine + "ribbon #" + str(saveit) + str(atomSpec) + "\r\n"
    if findWord("spheres", strInfo) >0:
        retLine = "~display " + strInfo[findWord(", ", strInfo) +2:] + "\r\n"
    return retLine
def show(strInfo, iterate):
    retLine = ''
    if findWord("cartoon", strInfo) > 0:
        retLine = ""
        if findWord("chain", strInfo) > 0:
            retLine = "ribbon #" + str(iterate) + ":." + strInfo[findWord("chain", strInfo)+6:findWord("chain", strInfo)+7].lower() + "\r\n"
    else:
        retLine = showSphere(strInfo, iterate)
    return retLine
def showSphere(strInfo, iterate):
    if findWord('.', strInfo) > 0:
        strRet = strInfo[findWord("chain", strInfo)+6:findWord("chain", strInfo)+7].lower()
        strRet = "#" + str(iterate) + ":." + strRet
        strReturn = "display " + strRet + "\r\n" + "repr sphere " + strRet + "\r\n"
    else:
        strRet = strInfo[findWord(", ", strInfo)+2:]
        strReturn = "display " + strRet + "\r\n" + "repr sphere " + strRet + "\r\n"
    return strReturn
def color(strInfo, iterate):
    if findWord(".", strInfo) < 0:
        iterate = strInfo[findWord(", ", strInfo)+2:]
    if findWord(".", strInfo) > 0:
        iterate = "#" + str(iterate)
    if findWord("gray10", strInfo) > 0:
        strCol = "color #191919 " + str(iterate)
    if findWord("white", strInfo) > 0:
        strCol = "color #FFFFFF " + str(iterate)
    if findWord("chain", strInfo) > 0:
        strCol = strCol + ":."+ strInfo[(findWord("chain", strInfo)+6):(findWord("chain", strInfo)+7)].lower()
    if findWord("resi", strInfo) > 0:
        print "resi found to be colored, FIX ERROR DUDE!"
    return strCol
def spec(strInfo, iterate):
    saveStr = strInfo
    strInfo1 = strInfo[findWord("chain ",strInfo):] ##getchain
    strInfo2 = "rainbow #" + str(iterate)
    if iterate < -1:
        strInfo2 = "rainbow #" + str(iterate)[1:]
    strChain =  "." + strInfo1[6:7].lower()
    if len(strInfo2) > 1:
        strInfo1 = strInfo[findWord("resi ",strInfo):]
        strInfo3 = strInfo2 + ":" + strInfo1[5:] + strChain
        if iterate < 0:
            strInfo3 = strInfo2 + ":" + strChain +  ":" + strInfo1[5:]
        if iterate == -1:
            strInfo3 = ":" + strInfo1[5:] + "" + strChain
            print strInfo3
        strInfo2 = strInfo3
        if iterate >0 and findWord("chain", saveStr) < 1:
            strInfo2 = strInfo2[7:]
            strInfo2 = "color #250421" + strInfo2
    return strInfo2
def split(strInfo, iterate):
    strin= "mmaker #0" + align(strInfo[findWord(", ", strInfo)+1:],iterate)
    return strin + " #" + str(iterate) + align(strInfo[:findWord(", ", strInfo)], iterate) + " pair ss iter false"
def align(strInfo, iterate):
    saveit = iterate
    str1 = spec(strInfo, -2)
    print "str1 " + str1
    str2 = str1[9+len(str(saveit)):]
    print "str2 " + str2
    return str2
def pairFit(strInfo, iterate):
    strin= "match #0" + pFit(strInfo[findWord(", ", strInfo)+1:],iterate)
    return strin + " #" + str(iterate) + pFit(strInfo[:findWord(", ", strInfo)], iterate) + " active"
def pFit(strInfo, iterate):
    strChain = strInfo[findWord("//", strInfo)+1:].lower()
    strChainLetter = strChain[1:2]
    ## = ":." + strChain[1:2]
    strRes = strChain[findWord("/", strChain)+1:]
    strRes = strRes[findWord("/", strChain)+2:]
    strReturn = ":" + strRes[:findWord("/", strRes)] + "." + strChainLetter
    if len(strRes) > 0:
        strMol = strRes[findWord("/", strRes)+1:]
        strReturn = strReturn + "@" + strMol
    return strReturn
def sele(strInfo, iterate):
    retLine = ''
    name = strInfo[5:findWord(", ", strInfo)]
    if findWord('chain', strInfo) > 0:
        retLine = recSelectChain(strInfo, iterate)
    if findWord(', het', strInfo) >0:
        retLine = "select " + ":/isHet"  #:/isHet
    return retLine + "\r\nnamesel " + name + "\r\n" + "\r\n"
def recSelectChain(strInfo, iterate):
    decString = strInfo
    ##print molList
    modNum = molList.index(decString[findWord(", ", decString)+2:findWord(".", decString)])
    decString = decString[findWord("chain ", decString) + 6:]
    retString = "select #" + str(modNum) + ":." + decString[:1].lower()
    while len(decString) > 2:
        modNum = molList.index(decString[4:findWord(".", decString)])
        decString = decString[findWord("chain ", decString) + 6:]
        retString = retString + " #" + str(modNum) + ":." + decString[:1].lower()
    return retString
def findWord(word, stringFind):
    index = stringFind.find(word)
    return index
##def getFilePath():0
##    print filepath[:-len(str(fileExtension))] +".txt"
##    return filepath[:-len(str(fileExtension))] +".txt"