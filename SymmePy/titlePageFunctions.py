#################################################
# 15-112-m18 Term Project: Title Page Mode
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################
from brushClass import *

#click to switch modes
def titlePageMousePressed(event, data):
    x, y=event.x, event.y
    xBoxStart, xBoxEnd=data.width//4, 3*data.width//4
    xBoxMid=(xBoxStart+xBoxEnd)/2
    topBox,midBox,bottBox=data.height*5/8, data.height*6/8, data.height*7/8
    if x>=xBoxStart and x<=xBoxEnd:
        if y>=topBox and y<midBox:
            if x>xBoxMid: 
                data.sides, data.lastMode=2, "twoToMany"
                data.mode="twoToMany"
            else: 
                data.mode, data.lastMode="draw", "draw"
        elif y>=midBox and y<bottBox:
            data.mode="instructions"
            
#allows the background to be drawn and removed
def titlePageTimerFired(data):
    list=data.ogTitleList
    data.titleCount+=1
    if data.titleCount%5==0 and data.titleCount<51: #does this 10 times
        line=list.pop(0) #removes first element
        data.titleList.append(line) #draws it
    elif data.titleCount%5==0 and data.titleCount>71: #does this 10 times
        line=data.titleList.pop() 
        list.append(line)
        if data.titleCount==120: 
            data.titleCount=0 #allows you to restart
    
###Drawing functions
#draws the title page, includes title and modes
def titlePageRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="black")
    createBackground(canvas, data)
    createSymmePy(canvas, data)
    createTitleBoxes(canvas, data)
   
#creates the background
def createBackground(canvas, data):
    originx, originy=data.width//2, data.height//2
    dist=((data.width//2)**2+(data.height//2)**2)**0.5
    gridx=originx+dist*math.cos(data.gridAngle)
    gridy=originy+dist*math.sin(data.gridAngle)
    data.gridList=[(originx, originy), (gridx, gridy)]
    gridLines=Line(data.gridList, "grey", 1, 8)
    gridLines.draw(canvas, data) 
    for item in data.titleList:
        item.draw(canvas, data)

#Creates the "SymmePy" title text    
def createSymmePy(canvas, data):
    l, r=13*data.width/40, 27*data.width/40
    t, b=data.width/5, 13*data.width/40
    canvas.create_rectangle(l, t, r, b, fill="black", width=0)
    cenX, titleCenY=data.width//2, data.height//4
    tF, w="Futura 60", "white"
    canvas.create_text(cenX, titleCenY, text="SymmePy", font=tF, fill=w)
    
#creates the boxes for other modes
def createTitleBoxes(canvas, data):
    tF, w, b="Futura 60", "white", "black"
    cenX, bS, topBox=data.width/2, data.width//4, data.height*5/8
    midBox, botBox, f=data.height*6/8, data.height*7/8, "Futura 48"
    canvas.create_rectangle(cenX-bS,topBox,cenX+bS,midBox,outline=w,fill=b,width=3)
    canvas.create_rectangle(cenX,topBox,cenX+bS,midBox,outline=w,fill=b,width=3)
    canvas.create_rectangle(cenX-bS,midBox,cenX+bS,botBox,outline=w,fill=b,width=3)
    midY1, midY2=(topBox+midBox)//2, (midBox+botBox)//2
    midY1a, midY1b=(midY1+topBox)/2, (midY1+midBox)/2
    midX1, midX2, ff=(cenX-bS+cenX)/2, (2*cenX+bS)/2, "Futura 40"
    canvas.create_text(midX1, midY1, text="Classic", font=f, fill=w)
    canvas.create_text(midX2, midY1a, text="Two to", font=ff, fill=w)
    canvas.create_text(midX2, midY1b, text="Many", font=ff, fill=w)
    canvas.create_text(cenX, midY2, text="Instructions", font=f, fill=w)
 
#creates the lines in the title page animation
def titleDrawings(data):
     y1=data.height/2
     white=[(21*data.width/40, y1), (21*data.width/40, 7*data.height/10)]
     pink=[(23*data.width/40, y1), (23*data.width/40, 31*data.height/40)]
     red=[(5*data.width/8, y1), (5*data.width/8, 17*data.height/20)]
     orange=[(27*data.width/40, y1), (27*data.width/40, 37*data.height/40)] 
     yellow=[(29*data.width/40, y1), (29*data.width/40, data.height)] 
     green=[(31*data.width/40, y1), (31*data.width/40, data.height)]
     blue1=[(33*data.width/40, y1), (33*data.width/40, 37*data.height/40)]
     blue2=[(7*data.width/8, y1), (7*data.width/8, 17*data.height/20)]
     purple=[(37*data.width/40, y1), (37*data.width/40, 31*data.height/40)]
     grey=[(39*data.width/40, y1), (39*data.width/40, 7*data.height/10)]
     
     list=[Line(white, "white", 2, 8), Line(pink, "maroon1", 2, 8),
     Line(red, "red", 2, 8), Line(orange, "orange", 2, 8),
     Line(yellow, "yellow", 2, 8), Line(green, "green2", 2, 8),
     Line(blue1, "LightSkyBlue3", 2, 8), Line(blue2, "DeepSkyBlue2", 2, 8),
     Line(purple, "DarkOrchid4", 2, 8), Line(grey, "gray56", 2, 8)]
     return list