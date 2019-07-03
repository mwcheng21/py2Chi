import sys
import os
import Tkinter
from Tkinter import Tk
import tkFileDialog
import subprocess
import time

sys.path.append("modules")
import convert
import convertError


def main():
    global fileExtension
    root = Tkinter.Tk()
    root.withdraw()
    direct = os.getcwd()
    dFile = open(("directorySave.txt"), "r+")
    filedata = dFile.read()
    dFile.close()
    if filedata != "":
        direct = filedata
    fileArray = tkFileDialog.askopenfilenames(initialdir=direct, parent = root,title='Select a file')
    fileString = str(fileArray)
    print fileArray
    lastSlash = 0
    iterator = 0
    begnum = 2
    for char in str(fileArray):
        if str(fileArray)[1] == "u":
            begnum = 3
        if str(fileArray)[iterator] == "/":
            lastSlash = iterator
        if str(fileArray)[iterator] == ",":
            break
        iterator += 1
    fileString = fileString[begnum:(lastSlash+1)]
    dFile = open('directorySave.txt', 'w')
    dFile.write(str(fileString))
    dFile.close()
    #print root.tk.splitlist(fileArray)
    for files in fileArray:
        filename = files
        fileExtension = os.path.splitext(filename)[1]
        if filename != "":
            print filename
            readFile(filename)
        #path = filename
        #subprocess.Popen('explorer "C:\Users\chengm\Downloads"')
##    cont = raw_input("Convert more files? y/n\r\n")
##    if cont.lower() == "y" or cont.lower() == "yes":
##        main()
def readFile(fileName):
    print "reading file"
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    #print content
    convert.main(content, fileName)
    convertError.main(fileName)
    time.sleep(5)
if __name__ == '__main__': main()
