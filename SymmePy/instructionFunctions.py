#################################################
# 15-112-m18 Term Project: Instructions Mode
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################
import random
from tkinter import *
from drawMouseHelper import *

#allows user to switch modes
def instructionsMousePressed(event, data):
    x, y=event.x, event.y
    t, b=data.height*7/8, data.height*15/16
    mL,mR,cL,cR=data.width/16,4*data.width/16,5*data.width/16,data.width/2
    tL,tR,nL,nR=9*data.width/16, 3*data.width/4,13*data.width/16, data.width
    if y>=t and y<=b:
        if x>=mL and x<mR: data.mode="titlePage"
        elif x>=cL and x<cR: 
            if data.lastMode!="draw": clearData(data)
            data.lastMode="draw"
            data.mode="draw"
        elif x>=tL and x<tR: 
            if data.lastMode!="twoToMany": clearData(data)
            data.sides=2
            data.lastMode="twoToMany"
            data.mode="twoToMany"
        elif x>=nL and x<=nR: data.mode="nextPage"
        
#allows the instructions title color to change
def instructionsTimerFired(data):
    data.instructionCount+=1
    if data.instructionCount==10:
        data.instructionColor=random.choice(data.colors[2:])
        data.instructionCount=0
    
###Drawing aspect (in alphabetical order after RedrawAll)
#overall instructions drawing
def instructionsRedrawAll(canvas, data):
    createInstructionsBackground(canvas, data)
    x, y, tex, f=data.width/2, data.height/16, "Welcome to SymmePy", "Futura 48"
    canvas.create_text(x, y,text=tex,font=f, fill=data.instructionColor)
    drawModeBoxes(canvas, data)
    createInstructions(canvas, data)
    
#creates instructions for brushes
def createBrushInstructions(canvas, data):
    x, y, tX=data.width//8, 5*data.height/32, 5*data.width/16
    canvas.create_text(x, y, text="Brushes:", font=data.font)
    l, r, t, b=data.width/16, 3*data.width/16, data.height/8, 3*data.height/16
    canvas.create_rectangle(l, t, r, b, outline="green2", width=2)
    y1, y2, y3= 5*data.height/32, 7*data.height/32, 9*data.height/32
    tex1="  Curvy: Can draw free-form!"
    tex2="  Line: Everything drawn will be a line (no curvature)"
    tex3="  Eraser: If you want to erase part of what is drawn"
    canvas.create_text(tX, y1, text=tex1, font=data.font, anchor="w")
    canvas.create_text(tX, y2, text=tex2, font=data.font, anchor="w")
    canvas.create_text(tX, y3, text=tex3, font=data.font, anchor="w")
    createIndBrushes(canvas, data)

#creates instruction for brush size
def createBrushSize(canvas, data):
    x, y= data.width//16, 11*data.height/32
    canvas.create_text(x, y, text="Brush Size:", font=data.font, anchor="w")
    t, b, x2=5*data.height/16, 6*data.height/16, 3*data.width/16
    canvas.create_rectangle(x, t, x2, b, outline="DarkOrchid4", width=2)
    tex="  Use the up or down keys, size between 1 and 50"
    canvas.create_text(x2, y, text=tex, font=data.font, anchor="w")

#creates instructions for choosing colors
def createColors(canvas, data):
    x, y, tex=data.width/4, 23*data.height/32, "Brush and Background Colors:"
    canvas.create_text(x, y, text=tex, font=data.font)
    l,t,r,b=data.width/16, 11*data.height/16, 7*data.width/16, 3*data.height/4
    canvas.create_rectangle(l, t, r, b, outline="DeepSkyBlue2", width=2)
    x2, tex=7*data.width/16, "  Click to choose colors, options below"
    canvas.create_text(x2, y, text=tex, font=data.font, anchor="w")
    colT, colB, numColors=3*data.height/4, 13*data.height/16, 16
    for i in range(numColors):
        x1, x2=(i)*data.width/16, (i+1)*data.width/16
        canvas.create_rectangle(x1, colT, x2, colB, fill=data.colors[i])
    
#creates instructions for erasing
def createErase(canvas, data):
    x, y=data.width/8, 19*data.height/32
    r, data.l=data.width/16, 3*data.width/16
    canvas.create_text(x, y, text="Undo:", font=data.font)
    tex='  Press "U" or click on box to undo the last move in all sections'
    canvas.create_text(data.l, y, text=tex, font=data.font, anchor="w")
    colors=["PeachPuff4", "red"]
    for i in range(2):
        t, b=(9+i)*data.height/16, (10+i)*data.height/16
        canvas.create_rectangle(data.l, t, r, b, outline=colors[i], width=2)

#creates instructions for showing gridlines
def createGrid(canvas, data):
    x, y= data.width/8, 13*data.height/32
    canvas.create_text(x, y, text="Gridlines:", font=data.font)
    l=3*data.width/16,
    tex='  Press "L" or click on the box to show or hide gridlines'
    canvas.create_text(l, y, text=tex, font=data.font, anchor="w")
    t, b, x1=6*data.height/16, 7*data.height/16, data.width/16
    canvas.create_rectangle(x1, t, l, b, outline="magenta2", width=2)
    y2=15*data.height/32
    moreTex="  Click on box and then move up/down to change angle"
    canvas.create_text(l, y2, text=moreTex, font=data.font, anchor="w")
    
#creates brushes (line/curve)
def createIndBrushes(canvas, data):
    lx1, lx2=(3*data.width/16)+5, (5*data.width/16)-5
    ly1, ly2=(3*data.height/16)+5, (data.height/4)-5
    canvas.create_line(lx1, ly2, lx2, ly1, width=2)
    ax1, ax2, ax3=(3*data.width/16)+5, data.width/4, (5*data.width/16)-5
    ay1, ay2=(data.height/8)+5, (3*data.height/16)-5
    canvas.create_arc(ax1,ay1,ax2,ay2,start=180, extent=180, style=ARC, width=2)
    canvas.create_arc(ax2,ay1,ax3,ay2,start=0, extent=180, style=ARC, width=2)
    h1, h2=data.height/4, 5*data.height/16
    midx, midy=(lx1+lx2)/2, (h1+h2)/2
    canvas.create_rectangle(lx1, h1, lx2, h2, fill="black")
    canvas.create_text(midx, midy, text="Bye!", 
    font="Chalkduster 20", fill="white")
    
#creates actual instructions text
def createInstructions(canvas, data):
    data.font="Futura 20"
    createBrushInstructions(canvas, data)
    createBrushSize(canvas, data)
    createColors(canvas, data)
    createSides(canvas, data)
    createGrid(canvas, data)
    createErase(canvas, data)
    createRestart(canvas, data)
    
#creates the white backgound and grid
def createInstructionsBackground(canvas, data):
    canvas.create_rectangle(0,0, data.width, data.height, fill="white",width=0)
    gridx, gridy, g=data.width/16, data.height/16, "gainsboro"
    for i in range(1, 16):
        canvas.create_line(0, i*gridy, data.width, i*gridy, fill=g)
        canvas.create_line(i*gridx, 0, i*gridx, data.height, fill=g)
        
#creates instructions for restarting
def createRestart(canvas, data): 
    x, y= data.width/8, 21*data.height/32
    canvas.create_text(x, y, text="Restarting:", font=data.font)
    tex="  Press escape or click on box to restart"
    canvas.create_text(data.l, y, text=tex, font=data.font, anchor="w")
    
#creates instructions for changing sides    
def createSides(canvas, data):
    x, y=5*data.width/32, 17*data.height/32
    canvas.create_text(x, y, text="# of Sections:", font=data.font)
    l, t, r, b=data.width/16, data.height/2, data.width/4, 9*data.height/16
    canvas.create_rectangle(l, t, r, b, outline="orange", width=2)
    tX=data.width/4
    tex='  Use left or right keys to change # of sections, min 2, max 20'
    canvas.create_text(tX, y, text=tex, font=data.font, anchor="w")
    
#draws main menu and draw functions, may change later?
def drawModeBoxes(canvas, data):
    boxTop, boxBot=data.height*7/8, data.height*15/16
    mL, mR=data.width/16, 4*data.width/16
    midY, c, f=(boxTop+boxBot)/2, "gainsboro", "Futura 22"
    canvas.create_rectangle(mL, boxTop, mR, boxBot, fill=c)
    cL, cR=5*data.width/16, data.width/2
    canvas.create_rectangle(cL, boxTop, cR, boxBot, fill=c)
    tL,tR=9*data.width/16, 3*data.width/4
    canvas.create_rectangle(tL, boxTop, tR, boxBot, fill=c)
    nL, nR=13*data.width/16, data.width
    canvas.create_rectangle(nL, boxTop, nR, boxBot, fill=c)
    midMen, midClass, midTwo, midNex=(mL+mR)/2, (cL+cR)/2, (tL+tR)/2, (nL+nR)/2
    canvas.create_text(midMen, midY, text="Main Menu", font=f)
    canvas.create_text(midClass, midY, text="Classic Mode", font=f)
    canvas.create_text(midTwo, midY, text="Two to Many", font=f)
    canvas.create_text(midNex, midY, text="Next Page", font=f)