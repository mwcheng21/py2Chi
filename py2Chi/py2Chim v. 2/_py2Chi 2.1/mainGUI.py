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

def wait():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if b1.collidepoint(pos):## or b6.collidepoint(pos):
                root = Tkinter.Tk()
                root.withdraw()
                fileArray = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
                #print root.tk.splitlist(fileArray)
                for files in fileArray:
                    filename = files
                    fileExtension = os.path.splitext(filename)[1]
                    if filename != "":
                        readFile(filename)
                #subprocess.Popen('explorer "C:\path\of\folder"')

def main():
    global b1, running, BLACK, WHITE, basicFont, fileExtension
    running = True
    displayFlags = HWSURFACE
    displayFlags = displayFlags|RESIZABLE
    displayFlags = displayFlags|DOUBLEBUF
    try:
        pygame.init()
    except Exception, e:
        print "Cannot initialize pyGame:"
        print e
        sys.exit(-1)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    basicFont = pygame.font.SysFont(None, 30, bold = True, italic=False)
    fileExtension = ""
    windowSurface = pygame.display.set_mode((322, 126),displayFlags)
    windowSurface.fill(WHITE)
    pygame.display.set_caption('MC Chimera <--> pyMol')
    rect = b1 = pygame.draw.rect(windowSurface, WHITE, (125, 30, 69, 66), 2)
    #b6 = drawText(windowSurface, "upload", BLACK, rect, basicFont, aa=True, bkg=None)
    upload = pygame.image.load('upload.png')
    windowSurface.blit(upload,(125,30)) 
    pygame.display.update()
    pygame.display.flip()
    while running:
        wait()
def terminate():
    pygame.quit()
    sys.exit(0)
def readFile(fileName):
    print "reading file"
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    convert.main(content, fileName)
    
if __name__ == '__main__': main()
