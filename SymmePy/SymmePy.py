#################################################
# 15-112-m18 Term Project: Main Page
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################
from tkinter import *
import math
import random

from titlePageFunctions import *
from instructionFunctions import *
from drawingFunctions import *
from drawingHelperFunctions import *
from drawMouseHelper import *
from brushClass import *
from rotateFunctions import *
from twoToManyFunctions import *
from nextPageFunctions import *

####################################
#Overall functions
####################################
#initial data
def init(data):
    data.titleCount, data.titleList=0, []
    data.ogTitleList=titleDrawings(data)
    data.instructionCount, data.instructionColor=0, "black"
    data.lastPage=None
    data.mode="titlePage"
    clearData(data) #function is also used when the user presses "restart"
    data.curvePt, data.tempList=[], []
    data.type="curve" #curve, line, or eraser
    data.lastMode="draw"
    
    data.colors=["black", "white", "gray56", "PeachPuff4", "thistle1", 
    "maroon1", "red","orange", "yellow", "green2", "Forest Green",
    "LightSkyBlue3", "DeepSkyBlue2", "Royal Blue", "plum3", "DarkOrchid4"]
    
    
#keyPressed functions
def keyPressed(event, data):
    if data.mode=="titlePage": pass
    elif data.mode=="instructions": pass
    elif data.mode=="nextPage": pass
    elif data.mode=="draw": drawKeyPressed(event, data) 
    elif data.mode=="rotate": rotateKeyPressed(event, data)
    elif data.mode=="twoToMany": drawKeyPressed(event, data)
    
#redrawAll functions defined in each page
def redrawAll(canvas, data):
    if data.mode=="titlePage": titlePageRedrawAll(canvas, data)
    elif data.mode=="instructions": instructionsRedrawAll(canvas, data)
    elif data.mode=="nextPage": nextPageRedrawAll(canvas, data)
    elif data.mode=="draw": drawRedrawAll(canvas, data)
    elif data.mode=="rotate": rotateRedrawAll(canvas, data)
    elif data.mode=="twoToMany": twoToManyRedrawAll(canvas, data)
    
#timerFired is needed for the title page animation, the color in instructions
#and to rotate the drawing in rotate mode
def timerFired(data):
    if data.mode=="titlePage": titlePageTimerFired(data)
    elif data.mode=="instructions": instructionsTimerFired(data)
    elif data.mode=="nextPage": instructionsTimerFired(data)
    elif data.mode=="draw": pass
    elif data.mode=="rotate": rotateTimerFired(data)
    elif data.mode=="twoToMany": pass
    
#different types of mouse usage is used (click, hold, release)
#all modes deal specifically with mousePressed
def mousePressed(event, data):
    if data.mode=="titlePage": titlePageMousePressed(event, data)
    elif data.mode=="instructions": instructionsMousePressed(event, data)
    elif data.mode=="draw": drawClickMousePressed(event, data)
    elif data.mode=="twoToMany": drawClickMousePressed(event, data)
    elif data.mode=="rotate": rotateMousePressed(event, data)
    elif data.mode=="nextPage": nextPageMousePressed(event, data)

####################################
#Run Function
#CITATION: Code adapted from the 112 website
#          Slightly modified to allow for different mouse functions
####################################

def run(width=800, height=800):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()
        
    #deals with functions that require clicking (as opposed to dragging)
    def mousePressedClickWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
        
    #deals with functions that require holding down and dragging
    def mousePressedHoldWrapper(event, canvas, data):
        drawMouseHeld(event, data)
        redrawAllWrapper(canvas, data)
        
    #deals with functions that need to take into account when mouse is released
    def mousePressedReleasedWrapper(event, canvas, data):
        drawMouseReleased(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay=100
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events 
    redrawAllWrapper(canvas, data)
    root.bind("<Button-1>", lambda event:
        mousePressedClickWrapper(event, canvas, data))
    root.bind("<B1-Motion>", lambda event: 
        mousePressedHoldWrapper(event, canvas, data))
    root.bind("<B1-ButtonRelease>", lambda event:
        mousePressedReleasedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
        keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()

#End Citation