import pygame
from pygame.locals import *
import sys
import os
import Tkinter
from Tkinter import Tk
import tkFileDialog
import subprocess


sys.path.append("modules")
import writeText
import convert

def main():
    global fileExtension
    root = Tkinter.Tk()
    root.withdraw()
    fileArray = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
    #print root.tk.splitlist(fileArray)
    for files in fileArray:
        filename = files
        fileExtension = os.path.splitext(filename)[1]
        if filename != "":
            readFile(filename)
##        path = str(convert.getFilePath())
##        print path
##        subprocess.Popen(r'explorer path /select, path')
def readFile(fileName):
    print "reading file"
    print "file extension " + fileExtension 
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    #print content
    convert.main(content, fileName)
    
main()
