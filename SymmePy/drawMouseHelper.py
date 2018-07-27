#################################################
# 15-112-m18 Term Project: Drawing Mode mouse/key Helper Functions
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################

###For ease of readability/search, functions are mostly in alphabetical order

#allows user to click on changing features
def checkFeatures(x, data):
    grid1, grid2=13*data.width/20, 61*data.width/80
    if x>=grid1 and x<grid2: 
        data.changeGrid=True
    restart1, restart2= 7*data.width/8, 31*data.width/32
    if x>=restart1 and x<=restart2: 
        clearData(data)
        if data.mode=="twoToMany": data.sides=2
    erase1, erase2=grid2, restart1
    if x>=erase1 and x<erase2: eraseLastThing(data)
    brush1, brush2=data.width/32, 7*data.width/40
    if x>=brush1 and x<brush2:
        data.changeBrush=True
    color1,bothColors,back=11*data.width/40,2*data.width/5,21*data.width/40
    if x>=color1 and x<bothColors and not data.changeBackground:
        data.changeColor=True
    if x>=bothColors and x<back and not data.changeColor:
        data.changeBackground=True

#shows/hides grid
def checkGrid(data):
    if data.grid==True: data.grid=False
    elif data.grid==False: data.grid=True

#turns layers on and off
def checkLayers(x, data): 
    La1, La2=5*data.width/16, 7*data.width/16
    Lb1, Lb2=La2, 9*data.width/16
    Lc1, Lc2=Lb2, 11*data.width/16
    if x>=La1 and x<La2: checkLayerA(data)
    elif x>=Lb1 and x<Lb2: checkLayerB(data)
    elif x>=Lc1 and x<Lc2: checkLayerC(data)
            
#allows user to turn "on or off" Layer A
def checkLayerA(data):
    if data.layerA==False: 
        data.layerA=True
        data.layerList.append("LayerA")
    else: 
        data.layerA=False
        data.layerList.remove("LayerA")
        
#allows user to turn "on or off" Layer B
def checkLayerB(data):
    if data.layerB==False: 
        data.layerB=True
        data.layerList.append("LayerB")
    else: 
        data.layerB=False
        data.layerList.remove("LayerB")
        
#allows user to turn "on or off" Layer C
def checkLayerC(data):
    if data.layerC==False: 
        data.layerC=True
        data.layerList.append("LayerC")
    else: 
        data.layerC=False
        data.layerList.remove("LayerC")

#checks if user wants to return to main menu or instructions
#if click main menu, the drawing is lost
def checkModes(x, data):
    data.menuL, data.menuR=data.width//32, 7*data.width/40
    data.helpL, data.helpR=data.menuR, 5*data.width//16
    if x>=data.menuL and x<data.menuR: 
        data.mode="titlePage"
        clearData(data)
    elif x>=data.helpL and x<=data.helpR: 
        data.mode="instructions"

#checks to see if rotate or two-to-many
def checkOtherModes(x, data):
    rot1, rot2=11*data.width/16, 13*data.width/16
    two1, two2=rot2, 31*data.width/32
    if x>=rot1 and x<rot2:
        data.lastMode=data.mode
        data.timerDelay=50
        data.mode="rotate"
    elif x>=two1 and x<=two2:
        if data.mode=="draw": 
            data.lastMode="twoToMany"
            data.mode="twoToMany"
            clearData(data)
            data.sides=2
        elif data.mode=="twoToMany": 
            data.lastMode="draw"
            data.mode="draw"
            clearData(data)

#allows user to choose between line and curved brush
def chooseBrush(x, y, data):
    startx, endx=data.cLeft, data.width//4
    if x>=startx and x<=endx:
        erase1, erase2=12*data.height/16, 13*data.height/16
        line1, line2=erase2, 14*data.height/16
        curve1, curve2=line2, 15*data.height/16
        if y>=erase1 and y<erase2: data.type="eraser"
        elif y>=line1 and y<line2: data.type="line"
        elif y>=curve1 and y<=curve2: data.type="curve"
        if y>=erase1 and y<=curve2: data.changeBrush=False
    

#allows user to choose which color for background/brush color
def chooseColor(x, y, data): 
    startX, startY=3*data.width//8, 3*data.height//8
    endX, endY=5*data.width//8, 5*data.height//8
    if x>startX and y>startY and x<endX and y<endY:
        nx, ny= x-startX, y-startY
        i, j, boxes= ny//50, nx//50, 4 #i is rows, j is cols
        color=data.colors[(boxes)*i+j]
        if data.changeColor:
            data.brushC=color
            data.changeColor=False
        elif data.changeBackground:
            data.backC=color
            data.changeBackground=False

#essentially initializes data
def clearData(data):
    data.listA, data.listB, data.listC=[], [], []
    data.backC, data.brushC="white", "black"
    data.sides, data.size=6, 1
    data.gridAngle, data.grid, data.changeGrid=0, True, False
    data.changeBrush, data.changeColor=False, False
    data.changeBackground=False
    data.layerA, data.layerB, data.layerC=True, False, False
    data.layerList=["LayerA"]
    data.rotCount, data.velocity, data.rotAngle=0, 0, 0
        

#creates "permanent" strokes on canvas (after releases mouse)
def drawStuff(canvas, data):
    for layer in data.layerList: #so in order of being clicked
        if layer=="LayerA":
            for item in data.listA:
                item.draw(canvas, data)
        elif layer=="LayerB":
            for item in data.listB:
                item.draw(canvas, data)
        elif layer=="LayerC":
            for item in data.listC:
                item.draw(canvas, data)

#creates drawing on canvas before user releases mouse
def drawTempStuff(canvas, data):
    if len(data.tempList)==0: pass
    for item in data.tempList:
        item.draw(canvas, data)
    
#removes the last thing drawn, if any
#undos move in last layer drawn (can click between layers to undo)
def eraseLastThing(data):
    length=len(data.layerList)
    if length>=1:
        last=data.layerList[length-1]
        if last=="LayerA":
            length=len(data.listA)
            if length>=1: data.listA.pop()
        elif last=="LayerB":
            length=len(data.listB)
            if length>=1: data.listB.pop()
        elif last=="LayerC":
            length=len(data.listC)
            if length>=1: data.listC.pop()
    
#returns True if it's paused, False if it isn't
def isPaused(data): 
    opt1, opt2=data.changeBrush, data.changeColor
    opt3, opt4=data.changeBackground, data.changeGrid
    return (opt1 or opt2 or opt3 or opt4)