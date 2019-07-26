#################################################
# 15-112-m18 Term Project: Brush Class (OOP)
# Your Name: Juliette Wong
# Your Andrew ID: jnwong
# TP Mentor: Jenny Yu
#################################################

import math

#overall class
class Brush(object):
    def __init__(self, points, color, width, sides):
        self.points=points
        self.color=color
        self.width=width
        self.sides=sides
    def getPoints(self):
        return self.points
    
#freehand drawing
class Curve(Brush):
    def draw(self, canvas, data):
        c, w, s=self.color, self.width, self.sides
        points=len(self.points)
        cx, cy=data.width//2, data.height//2
        if points<5: pass
        if points>=5:
            for i in range(s):
                pointList=[]
                for point in self.points:
                    x, y=point[0], point[1]
                    xp, yp=x-cx, y-cx
                    if xp==0: angle=math.pi/2
                    else: angle=math.atan(yp/xp)
                    (nx, ny)=findNewCoord(s, cx, cy, xp, yp, angle, i, data)
                    pointList.append((nx, ny))
                canvas.create_line(pointList, fill=c, width=w, smooth=True)
    
#drawing only straight lines
#FIX "local variable angle1 reference dbefore assignment"?
class Line(Brush):
    def draw(self, canvas, data):
        length=len(self.points)
        if length<2: pass
        if length>=2:
            s, pi, c, w=self.sides, math.pi, self.color, self.width
            x1, y1=self.points[0][0], self.points[0][1]
            x2, y2=self.points[length-1][0], self.points[length-1][1]
            cx, cy=data.width//2, data.height//2
            #SUBTRACT TO MAKE cx/cy the "origin"
            x1p, x2p, y1p, y2p=x1-cx, x2-cx, y1-cy, y2-cy
            if x1p==0: 
                angle1=(math.pi/2)
            else: angle1=math.atan(y1p/x1p)
            if x2p==0: angle2=math.pi/2
            else: angle2=math.atan(y2p/x2p)
            for i in range(s):
                (nx1, ny1)=findNewCoord(s, cx, cy, x1p, y1p, angle1, i, data)
                (nx2, ny2)=findNewCoord(s, cx, cy, x2p, y2p, angle2, i, data)
                canvas.create_line(nx1, ny1, nx2, ny2, fill=c, width=w)
                
    
#Uses givens rotations to find the new x and y values
#(idea taken from my current math research)
def findNewCoord(s, cx, cy, xp, yp, angle, i, data):
    nAng=angle+(i*2*math.pi/s)
    cAng=nAng-angle
    nx=int(cx+xp*math.cos(cAng+data.rotAngle)-yp*math.sin(cAng+data.rotAngle))
    ny=int(cy+xp*math.sin(cAng+data.rotAngle)+yp*math.cos(cAng+data.rotAngle))
    return (nx, ny)
    
#"special" type of curve used for twoToMany mode
class SideCurve(Curve):
    def draw(self, canvas, data):
        c, w, s=self.color, self.width, data.sides
        points=len(self.points)
        cx, cy=data.width//2, data.height//2
        if points<5: pass
        if points>=5:
            for i in range(s):
                pointList=[]
                for point in self.points:
                    x, y=point[0], point[1]
                    xp, yp=x-cx, y-cx
                    if xp==0: angle=math.pi/2+data.rotAngle
                    else: angle=math.atan(yp/xp)+data.rotAngle
                    (nx, ny)=findNewCoord(s, cx, cy, xp, yp, angle, i, data)
                    pointList.append((nx, ny))
                canvas.create_line(pointList, fill=c, width=w, smooth=True)
    
#"special" type of curve used for twoToMany mode
class SideLine(Line):
    def draw(self, canvas, data):
        length=len(self.points)
        if length<2: pass
        if length>=2:
            s, pi, c, w=data.sides, math.pi, self.color, self.width
            x1, y1=self.points[0][0], self.points[0][1]
            x2, y2=self.points[length-1][0], self.points[length-1][1]
            cx, cy=data.width//2, data.height//2
            #Subtract to make cx/cy the "origin"
            x1p, x2p, y1p, y2p=x1-cx, x2-cx, y1-cy, y2-cy
            if x1p==0: 
                ang1=math.pi/2
            else: ang1=math.atan(y1p/x1p)
            if x2p==0: ang2=math.pi/2
            else: ang2=math.atan(y2p/x2p)
            for i in range(s):
                (nx1, ny1)=findNewCoord(s, cx, cy, x1p, y1p, ang1, i, data)
                (nx2, ny2)=findNewCoord(s, cx, cy, x2p, y2p, ang2, i, data)
                canvas.create_line(nx1, ny1, nx2, ny2, fill=c, width=w)
    
#eraser for general draw mode
class Eraser(Curve):
    def draw(self, canvas, data):
        c, w, s=data.backC, self.width, self.sides
        points=len(self.points)
        cx, cy=data.width//2, data.height//2
        if points<5: pass
        if points>=5:
            for i in range(s):
                pointList=[]
                for point in self.points:
                    x, y=point[0], point[1]
                    xp, yp=x-cx, y-cx
                    if xp==0: angle=math.pi/2
                    else: angle=math.atan(yp/xp)
                    (nx, ny)=findNewCoord(s, cx, cy, xp, yp, angle, i, data)
                    pointList.append((nx, ny))
                canvas.create_line(pointList, fill=c, width=w, smooth=True)

#eraser used for twoToMany mode
class SideEraser(Curve):
    def draw(self, canvas, data):
        c, w, s=data.backC, self.width, data.sides
        points=len(self.points)
        cx, cy=data.width//2, data.height//2
        if points<5: pass
        if points>=5:
            for i in range(s):
                pointList=[]
                for point in self.points:
                    x, y=point[0], point[1]
                    xp, yp=x-cx, y-cx
                    if xp==0: angle=math.pi/2
                    else: angle=math.atan(yp/xp)
                    (nx, ny)=findNewCoord(s, cx, cy, xp, yp, angle, i, data)
                    pointList.append((nx, ny))
                canvas.create_line(pointList, fill=c, width=w, smooth=True)