#################################################
# 15-112-m18 Term Project: Rotate Mode
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################
from drawingHelperFunctions import *
from drawMouseHelper import *

#allows user to user arrow keys to rotate the drawing and show/hide grid
def rotateKeyPressed(event, data):
    if event.keysym=="Up" or event.keysym=="Left":
        data.velocity+=1
        data.rotCount=0
        if data.velocity>=21: data.velocity=20
    elif event.keysym=="Down" or event.keysym=="Right":
        data.velocity-=1
        data.rotCount=0
        if data.velocity<=-21: data.velocity=-20
    elif event.keysym=="l":
        checkGrid(data)
    
#changes speed of rotation
def rotateTimerFired(data): 
    data.rotCount+=1
    if data.velocity==0: pass
    elif data.rotCount==(21-abs(data.velocity)):
        if data.velocity==abs(data.velocity): 
            data.rotAngle-=math.pi/20
            if data.rotAngle==2*math.pi:
                data.rotAngle=0
        else:
            data.rotAngle+=math.pi/20
            if data.rotAngle==-2*math.pi:
                data.rotAngle=0
        data.rotCount=0
        
#allows user to switch between sections
def rotateMousePressed(event, data): 
    l, t, r, b=data.width/16, 5, 5*data.width/16, data.height/16-5
    x, y=event.x, event.y
    if x>=l and x<=r and y>=t and y<=b:
        data.rotAngle=0
        if data.lastMode=="draw":
            data.mode="draw"
        elif data.lastMode=="twoToMany":
            data.mode="twoToMany"
        data.timerDelay=100
        data.velocity=0
        data.rotAng=0


###Drawing functions
#draws the overall screen
def rotateRedrawAll(canvas, data):
    createDrawingBoard(canvas, data)
    drawTempStuff(canvas, data)
    drawStuff(canvas, data)
    if data.grid==True:
        drawGrid(canvas, data)
    drawPillars(canvas, data)
    createBackButton(canvas, data)
    createVelocityTexts(canvas, data)
    
#creates button that returns to the drawing
def createBackButton(canvas, data): 
    l, t, r, b=data.width/16, 5, 5*data.width/16, data.height/16-5
    canvas.create_rectangle(l, t, r, b, fill="gainsboro")
    midX, midY=(l+r)/2, (t+b)/2
    canvas.create_text(midX, midY, text="Back to Drawing", font="Futura 20")

#shows user the speed at which the drawing is going
def createVelocityTexts(canvas, data): 
    l, r, t, b=11*data.width/16, 15*data.width/16, 5, data.height/16-5 
    canvas.create_rectangle(l, t, r, b, fill="gainsboro")
    vX,vY,vTex=(l+r)/2,data.height/32,"Velocity: %i" %(data.velocity)
    canvas.create_text(vX, vY, text=vTex, font="Futura 20")
    botL, botR=data.width/16, 15*data.width/16 
    botT, botB=15*data.height/16+5, data.height-5
    midX, midY=(botL+botR)/2, (botT+botB)/2
    vTex="Use the arrow keys to rotate your drawing! Press 'L' to show/hide grid"
    canvas.create_rectangle(botL, botT, botR, botB, fill="gainsboro")
    canvas.create_text(midX, midY, text=vTex, font="Futura 20")
        