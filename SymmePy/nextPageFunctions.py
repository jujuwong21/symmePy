#################################################
# 15-112-m18 Term Project: page 2 of instructions
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################
from instructionFunctions import *
from drawMouseHelper import *

#allows user to click between sections
def nextPageMousePressed(event, data):
    x, y, w, h=event.x, event.y, data.width, data.height
    px1, px2, py1, py2=data.startX, w/4, h/16, h/8
    if x>=px1 and x<=px2 and y>=py1 and y<=py2:
        data.mode="instructions"
    y1, y2, m1, m2=7*h/8, 15*h/16, w/8, 3*w/8
    c1, c2, t1, t2=7*w/16, 5*w/8, 11*w/16, 7*w/8
    if y>=y1 and y<=y2:
        if x>=m1 and x<=m2: data.mode="titlePage"
        elif x>=c1 and x<=c2:
            if data.lastMode!="draw": clearData(data)
            data.lastMode="draw"
            data.mode="draw"
        elif x>=t1 and x<=t2: 
            if data.lastMode!="twoToMany": clearData(data)
            data.sides=2
            data.mode="twoToMany"

###Drawing functions! (in alphabetical order after redrawllAll)

#overall drawing function for nextPage
def nextPageRedrawAll(canvas, data):
    data.startX, data.font, data.fill=data.width/16, "Futura 20", "gainsboro"
    createInstructionsBackground(canvas, data)
    firstPageInstructions(canvas, data)
    createNextPageText(canvas, data)
    createLayerText(canvas, data)
    createClassicText(canvas, data)
    createTwoToManyText(canvas, data)
    createRotateText(canvas, data)
    createButtons(canvas, data)
    
#creates buttons to switch between modes    
def createButtons(canvas, data): 
    w, h=data.width, data.height
    y1, y2, m1, m2=7*h/8, 15*h/16, w/8, 3*w/8
    c1, c2, t1, t2=7*w/16, 5*w/8, 11*w/16, 7*w/8
    yMid, mMid, cMid, tMid=(y1+y2)/2, (m1+m2)/2, (c1+c2)/2, (t1+t2)/2
    canvas.create_rectangle(m1, y1, m2, y2, fill=data.fill)
    canvas.create_text(mMid, yMid, text="Main Menu", font=data.font)
    canvas.create_rectangle(c1, y1, c2, y2, fill=data.fill)
    canvas.create_text(cMid, yMid, text="Classic Mode", font=data.font)
    canvas.create_rectangle(t1, y1, t2, y2, fill=data.fill)
    canvas.create_text(tMid, yMid, text="Two to Many", font=data.font)

#creates text that describes classic mode
def createClassicText(canvas, data): 
    w, h, f=data.width, data.height, data.font
    l, r, t, b=data.startX, w/4, 3*h/8, 7*h/16
    midx, midy1, midy2=(l+r)/2, (t+b)/2, 15*h/32
    canvas.create_rectangle(l, t, r, b, outline="plum3", width=2)
    canvas.create_text(midx, midy1, text="Classic Mode:", font=f)
    tex1="  Whatever is drawn in one section is drawn in corr. sections"
    tex2="  Changing # of sides will not affect what is previously drawn"
    canvas.create_text(r, midy1, text=tex1, font=f, anchor="w")
    canvas.create_text(r, midy2, text=tex2, font=f, anchor="w")    
    
#creates text that describes how to use layers    
def createLayerText(canvas, data):
    w, h=data.width, data.height
    l, r, t, b=data.startX, 3*w/16, 3*h/16, h/4
    canvas.create_rectangle(l, t, r, b, outline="Forest Green", width=2)
    midx, midy=(l+r)/2, (t+b)/2
    canvas.create_text(midx, midy, text="Layers:", font=data.font)
    x, y1, y2, y3=r, midy, 9*h/32, 11*h/32
    tex1="  Allows you to draw parts of drawing at a time w/o distraction"
    tex2="  Click on respective layers to hide or show layers"
    tex3="  Layers will be drawn in order of being clicked"
    canvas.create_text(x, y1, tex=tex1, font=data.font, anchor="w")
    canvas.create_text(x, y2, tex=tex2, font=data.font, anchor="w")
    canvas.create_text(x, y3, tex=tex3, font=data.font, anchor="w")
    
#creates title for next page mode
def createNextPageText(canvas, data):
    x, y, tex=5*data.width/8, 3*data.height/32, "Other Modes and Features"
    f, c="Futura 36", data.instructionColor
    canvas.create_text(x, y, text=tex, font=f, fill=c)
    
#creates text that describes rotate mode
def createRotateText(canvas, data):
    w, h, f=data.width, data.height, data.font
    l, r, t, b=data.startX, 3*w/16, 11*h/16, 3*h/4
    midx, midy1, midy2=(l+r)/2, (t+b)/2, 25*h/32
    canvas.create_rectangle(l, t, r, b, outline="Royal Blue", width=2)
    canvas.create_text(midx, midy1, text="Rotate:", font=f)
    tex1="  Use the up, down, left, or right keys to rotate the drawing!"
    tex2="  Returning to drawing will not affect what is already drawn"
    canvas.create_text(r, midy1, text=tex1, font=f, anchor="w")
    canvas.create_text(r, midy2, text=tex2, font=f, anchor="w")
    
#creates text that describes twoToMany mode
def createTwoToManyText(canvas, data):
    w, h, f=data.width, data.height, data.font
    l, r, t, b=data.startX, w/4, h/2, 9*h/16
    midx, midy1, midy2, midy3=(l+r)/2, (t+b)/2, 19*h/32, 21*h/32
    canvas.create_rectangle(l, t, r, b, outline="orange", width=2)
    canvas.create_text(midx, midy1, text="Two To Many:", font=f)
    tex1="  Changing # of sides affects EVERYTHING on the drawing board"
    tex2="  Ex: Going 2 sides to 10 sides makes drawing appear 5x more"
    tex3="  Still has same drawing features as in classic mode"
    canvas.create_text(r, midy1, text=tex1, font=f, anchor="w")
    canvas.create_text(r, midy2, text=tex2, font=f, anchor="w")
    canvas.create_text(r, midy3, text=tex3, font=f, anchor="w")
    
#creates button that allows user to return to first pg. of instructions
def firstPageInstructions(canvas, data): 
    l, r, t, b=data.startX, data.width/4, data.height/16, data.height/8
    canvas.create_rectangle(l, t, r, b, fill=data.fill)
    x, y=(l+r)/2, (t+b)/2
    canvas.create_text(x, y, text="Previous Page", font=data.font)