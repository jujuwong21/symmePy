#################################################
# 15-112-m18 Term Project: Drawing Mode redrawAll Helper Functions
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################

import math
from tkinter import *
from brushClass import *

###For organization, the functions are in alphabetical order

#creates boxes for brush type and brush size
def createBrushBoxes(canvas, data):
    left, mid, right=data.width//32, 7*data.width//40, 11*data.width//40
    c="gainsboro"
    canvas.create_rectangle(left, data.featT, mid, data.featB, fill=c)
    x=(left+2*mid/3)//2
    canvas.create_text(x, data.midFeat, text="Brush:", font="Futura 20")
    canvas.create_rectangle(mid, data.featT, right, data.featB, fill=c)
    canvas.create_text((mid+right)//2, data.midFeat, text="Size: %i" 
    %(data.size), font="Futura 20")
    drawLittleBrushIcon(canvas, data)
    
#creates boxes for brush color and background color
def createColorBoxes(canvas, data):
    left, mid, right=11*data.width//40, 2*data.width//5, 21*data.width//40
    c="gainsboro"
    x1, x2=(left+11*mid/12)//2, (mid+11*right/12)//2
    canvas.create_rectangle(left, data.featT, mid, data.featB, fill=c)
    canvas.create_text(x1, data.midFeat, text="Color:", font="Futura 20")
    colL, boxT=29*data.width/80, data.featT+10
    colR, boxB=colL+20, data.featB-10
    canvas.create_rectangle(colL, boxT, colR, boxB, fill=data.brushC)
    canvas.create_rectangle(mid, data.featT, right, data.featB, fill=c) 
    canvas.create_text(x2, data.midFeat, text="Bkgrd:", font="Futura 20")
    bkgdL, bkgdR=39*data.width//80, 41*data.width//80
    canvas.create_rectangle(bkgdL, boxT, bkgdR, boxB, fill=data.backC)

#creates the canvas (initially empty)
def createDrawingBoard(canvas, data):
    data.cTop, data.cBot=data.height//16, 15*data.height//16
    data.cLeft, data.cRight=data.width//16, 15*data.width//16
    canvas.create_rectangle(data.cLeft,data.cTop, data.cRight,data.cBot,
    fill=data.backC, outline="white")
    
#creates boxes for features (see below)
def createFeatures(canvas, data):
    data.featT, data.featB=data.cBot+5, data.width-5
    data.midFeat=(data.featT+ data.featB)//2
    createBrushBoxes(canvas, data)
    createColorBoxes(canvas, data)
    createOtherFeatures(canvas, data)
    
#creates boxes for layers A-C
def createLayerBoxes(canvas, data):
    midY, f=(data.mTop+data.mBot)/2, "Futura 20"
    La1, La2=5*data.width/16, 7*data.width/16
    Lb1, Lb2=La2, 9*data.width/16
    Lc1, Lc2=Lb2, 11*data.width/16
    midA, midB, midC=(La1+La2)/2, (Lb1+Lb2)/2, (Lc1+Lc2)/2
    if data.layerA: col1="yellow"
    else: col1="gainsboro"
    if data.layerB: col2="yellow"
    else: col2="gainsboro"
    if data.layerC: col3="yellow"
    else: col3="gainsboro"
    canvas.create_rectangle(La1, data.mTop, La2, data.mBot, fill=col1)
    canvas.create_text(midA, midY, text="Layer A", font=f)
    canvas.create_rectangle(Lb1, data.mTop, Lb2, data.mBot, fill=col2)
    canvas.create_text(midB, midY, text="Layer B", font=f)
    canvas.create_rectangle(Lc1, data.mTop, Lc2, data.mBot, fill=col3)
    canvas.create_text(midC, midY, text="Layer C", font=f)
    
#creates boxes for # of sides, gridlines, erase, and restart
def createOtherFeatures(canvas, data):
    left, mid1, mid2=21*data.width//40, 13*data.width//20, 61*data.width//80
    mid3, right, c=7*data.width/8, 31*data.width//32, "gainsboro"
    sideMid, gridMid=(left+mid1)//2, (mid1+mid2)//2
    eraseMid, restMid, f=(mid2+mid3)//2, (mid3+right)//2, "Futura 20"
    canvas.create_rectangle(left, data.featT, mid1, data.featB, fill=c)
    canvas.create_text(sideMid, data.midFeat, 
    text="Sides: %i" %(data.sides), font=f)
    canvas.create_rectangle(mid1, data.featT, mid2, data.featB, fill=c)
    canvas.create_text(gridMid, data.midFeat, text="Grid", font=f)
    canvas.create_rectangle(mid2, data.featT, mid3, data.featB, fill=c)
    canvas.create_text(eraseMid, data.midFeat, text="Undo", font=f)
    canvas.create_rectangle(mid3, data.featT, right, data.featB, fill=c)
    canvas.create_text(restMid, data.midFeat, text="Restart", font=f)
    
#creates boxes for rotate and two-to-many modes
def createOtherModeBoxes(canvas, data):
    rot1, rot2=11*data.width/16, 13*data.width/16
    two1, two2=rot2, 31*data.width/32
    midRot, midTwo, f=(rot1+rot2)/2, (two1+two2)/2, "Futura 20"
    g, midY="gainsboro", (data.mTop+data.mBot)/2
    canvas.create_rectangle(rot1, data.mTop, rot2, data.mBot, fill=g)
    canvas.create_text(midRot, midY, text="Rotate!", font=f)
    canvas.create_rectangle(two1, data.mTop, two2, data.mBot, fill=g)
    canvas.create_text(midTwo, midY, text="Two to Many", font=f)

#creates boxes for the top (modes and layers)
def createTopBoxes(canvas, data):
    createTopModeBoxes(canvas, data)
    createLayerBoxes(canvas, data)
    createOtherModeBoxes(canvas, data)
    
#create boxes for main menu and instructions
def createTopModeBoxes(canvas, data):
    data.mTop, data.mBot, g, f=5, data.cTop-5, "gainsboro", "Futura 20"
    midY=(data.mTop+data.mBot)//2
    data.menuL, data.menuR=data.width//32, 7*data.width/40
    midMenX=(data.menuL+data.menuR)//2
    canvas.create_rectangle(data.menuL,data.mTop,data.menuR,data.mBot,fill=g)
    canvas.create_text(midMenX, midY, text="Main Menu", font=f)
    data.helpL, data.helpR=data.menuR, 5*data.width//16
    midHelpX=(data.helpL+data.helpR)//2
    canvas.create_rectangle(data.helpL,data.mTop,data.helpR,data.mBot,fill=g)
    canvas.create_text(midHelpX, midY, text="Instructions", font=f)
    
#draws a curve, a line, or a letter "E" depending on brush type
def drawLittleBrushIcon(canvas, data):
    left, mid, right=data.width//32, 7*data.width//40, 11*data.width//40
    x1, y1, x2, y2=left+70, data.featT+10, mid-10, data.featB-10
    xmid, ymid=(x1+x2)//2, (y1+y2)//2
    xmidN, ymidN, xmidM, ymidM=xmid+5, ymid+5, xmid-2, ymid+2
    if data.type=="line":
        canvas.create_line(x1, y1, x2, y2, width=2)
    elif data.type=="curve":
        canvas.create_arc(x1, y1, xmidN, ymidN, start=135,
        extent=180, style=ARC, width=2)
        canvas.create_arc(xmidM, ymidM, x2, y2, start=-45, 
        extent=180, style=ARC, width=2)
    elif data.type=="eraser":
        canvas.create_text(xmid, (y1+y2)/2, text="E", font="Chalkduster 20")

#when clicked, draws the 2 brush options
def drawBrushOptions(canvas, data):
    x1, x2=data.cLeft, data.width//4
    xmid=(x1+x2)//2
    y1, y2=data.cBot-3*data.height/16, data.cBot
    canvas.create_rectangle(x1, y1, x2, y2, fill="gainsboro")
    textList=["Eraser", "made a mistake?", "Line Brush:", "straight lines only",
    "Curve Brush:", "draw freeform!"]
    for i in range(3):
        ny=y1+i*data.height/16
        midy1=ny+data.height/64
        midy2=ny + 3*data.height/64
        canvas.create_line(x1, ny, x2, ny)
        canvas.create_text(xmid, midy1, text=textList[2*i], font="Futura 16") 
        canvas.create_text(xmid, midy2,text=textList[(2*i)+1], font="Futura 16")

#when clicked, draws the color chart
def drawColorChart(canvas, data): 
    startX, endX=3*data.width/8, 5*data.width/8
    bigY1, bigY2=11*data.height/32, 21*data.height/32
    canvas.create_rectangle(startX, bigY1, endX, bigY2, fill="gainsboro")
    numBox, r, startY=4, 50, 3*data.height/8
    for i in range(numBox): #for rows
        for j in range(numBox): #for col
            color=data.colors[(numBox*i)+j]
            x1, y1=startX+r*j, startY+r*i 
            x2, y2=x1+r, y1+r
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    wordMid, wordTop, wordBot=data.width//2, 9*data.height/25, 16*data.height/25
    f="Futura 12"
    canvas.create_text(wordMid, wordTop, text="Choose a color!", font=f)
    if data.changeBackground:
        canvas.create_text(wordMid, wordBot, text="Background", font=f)
    elif data.changeColor:
        canvas.create_text(wordMid, wordBot, text="Brush Color", font=f)
    
#draws the grid lines
def drawGrid(canvas, data): 
    originx, originy=data.width//2, data.height//2
    dist=((data.width//2)**2+(data.height//2)**2)**0.5
    gridx=originx+dist*math.cos(data.gridAngle)
    gridy=originy+dist*math.sin(data.gridAngle)
    data.gridList=[(originx, originy), (gridx, gridy)]
    gridLines=Line(data.gridList, "grey", 1, data.sides)
    gridLines.draw(canvas, data)
    
#draws the notice to help move the grid
def drawGridHelp(canvas, data):
    tx, ty=data.width//2, data.height//32
    l, r=data.width//4, 3*data.width//4
    canvas.create_rectangle(l, data.mTop, r, data.mBot, fill="red") 
    tex="Use up and down to change angle! Press 'Return' when done."
    canvas.create_text(tx, ty, text=tex, font="Futura 14")

#creates the gray background for the project
def drawPillars(canvas, data):
    g="dim gray"
    canvas.create_rectangle(0, 0, data.cLeft, data.height+5, fill=g, width=0)
    canvas.create_rectangle(0, 0, data.width, data.cTop, fill=g, width=0)
    canvas.create_rectangle(0, data.cBot, data.width+5, data.height+5, 
    fill=g, width=0)
    canvas.create_rectangle(data.cRight, 0, data.width+5, data.height+5,
    fill=g, width=0)
    
    
