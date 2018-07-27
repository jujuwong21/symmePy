#################################################
# 15-112-m18 Term Project: Drawing Mode
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################

from drawingHelperFunctions import *
from drawMouseHelper import *
from brushClass import *
import math
import copy
    
#should be when you check different modes, "features" drop
def drawMouseHeld(event, data):
    if (data.mode=="draw" or data.mode=="twoToMany") and not isPaused(data):
        size=data.size
        sides=data.sides
        x, y=event.x, event.y
        #does it need to be in bounds??
        if y>=data.cTop and y<=data.cBot and x>=data.cLeft and x<=data.cRight:
            data.curvePt.append((x, y))
        length=len(data.tempList)
        if length>1: data.tempList.pop()
        if data.type=="curve":
            if data.mode=="draw":
                data.tempList.append(
                Curve(data.curvePt[1:], data.brushC, size, sides))
            elif data.mode=="twoToMany":
                data.tempList.append(
                SideCurve(data.curvePt[1:], data.brushC, size, sides))
        elif data.type=="line":
            if data.mode=="draw":
                data.tempList.append(
                Line(data.curvePt[1:], data.brushC, size, sides))
            elif data.mode=="twoToMany":
                data.tempList.append(
                SideLine(data.curvePt[1:], data.brushC, size, sides))
        elif data.type=="eraser":
            if data.mode=="draw":
                data.tempList.append(
                Eraser(data.curvePt[1:], data.brushC, size, sides))
            elif data.mode=="twoToMany":
                data.tempList.append(
                SideEraser(data.curvePt[1:], data.brushC, size, sides))
            
#can end outside of boundary, but won't draw
def drawMouseReleased(event, data):
    if (data.mode=="draw" or data.mode=="twoToMany") and not isPaused(data):
        tempLen, layerLen=len(data.tempList), len(data.layerList)
        if tempLen>1 and layerLen>=1:
            last=data.tempList[tempLen-1] #takes only the last tuple/class thing
            chosenLayer=data.layerList[layerLen-1]
            if chosenLayer=="LayerA":
                data.listA.append(last)
            elif chosenLayer=="LayerB":
                data.listB.append(last)
            elif chosenLayer=="LayerC":
                data.listC.append(last)
            data.curvePt=[]
            data.tempList=[] #clears tempList for next time

#see instructions for specific things
def drawKeyPressed(event, data):
    if event.keysym=="Up": 
        if data.changeGrid==True:
            data.gridAngle-=math.pi/180
            if data.gridAngle==-2*math.pi: data.gridAngle=0
        else: 
            data.size+=1
            if data.size>=50: data.size=50
    elif event.keysym=="Down":
        if data.changeGrid==True:
            data.gridAngle+=math.pi/180
            if data.gridAngle==2*math.pi: data.gridAngle=0
        else: 
            data.size-=1
            if data.size<=1: data.size=1
    elif event.keysym=="l": checkGrid(data)
    elif event.keysym=="Right": 
        data.sides+=1
        if data.sides>=20: data.sides=20
    elif event.keysym=="Left": 
        data.sides-=1
        if data.sides<=2: data.sides=2
    elif event.keysym=="u": eraseLastThing(data)
    elif event.keysym=="Escape": clearData(data)
    elif event.keysym=="Return": data.changeGrid=False
    
    
#overall function, creates background, canvas, and features
#All functions in drawingHelperFunctions
#create border so that the lines don't look like they go over
def drawRedrawAll(canvas, data):
    createDrawingBoard(canvas, data)
    drawStuff(canvas, data)
    drawTempStuff(canvas, data)
    if data.grid==True:
        drawGrid(canvas, data)
    drawPillars(canvas, data)
    createTopBoxes(canvas, data)
    createFeatures(canvas, data)
    if data.changeGrid==True:
        drawGridHelp(canvas, data)
    if (data.changeColor==True or data.changeBackground==True):
        drawColorChart(canvas, data)
    if data.changeBrush==True:
        drawBrushOptions(canvas, data)
        
#allows the user to click (as opposed to moving) for features/modes
def drawClickMousePressed(event, data):
    if data.mode=="draw" or data.mode=="twoToMany":
        x, y= event.x, event.y
        top, bot=(15*data.height//16)+5, data.height-5
        if (data.changeColor or data.changeBackground):
            chooseColor(x, y, data)
        if data.changeBrush:
            chooseBrush(x, y, data)
        if y>=top and y<=bot:
            checkFeatures(x, data)
        modeT, modeB=5, (data.height/16)-5
        if y>=modeT and y<=modeB:
            checkModes(x, data)
            checkOtherModes(x, data)
            if not isPaused(data):
                checkLayers(x, data)
        
        