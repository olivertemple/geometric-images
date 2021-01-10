import matplotlib.pyplot as plt
import math

def intersectLines( pt1, pt2, ptA, ptB ): 
    DET_TOLERANCE = 0.00000001

    # the first line is pt1 + r*(pt2-pt1)
    # in component form:
    x1, y1 = pt1;   x2, y2 = pt2
    dx1 = x2 - x1;  dy1 = y2 - y1

    # the second line is ptA + s*(ptB-ptA)
    x, y = ptA;   xB, yB = ptB
    dx = xB - x;  dy = yB - y

    DET = (-dx1 * dy + dy1 * dx)

    if math.fabs(DET) < DET_TOLERANCE: return (0,0,0,0,0)

    # now, the determinant should be OK
    DETinv = 1.0/DET

    # find the scalar amount along the "self" segment
    r = DETinv * (-dy  * (x-x1) +  dx * (y-y1))

    # find the scalar amount along the input line
    s = DETinv * (-dy1 * (x-x1) + dx1 * (y-y1))

    # return the average of the two descriptions
    xi = (x1 + r*dx1 + x + s*dx)/2.0
    yi = (y1 + r*dy1 + y + s*dy)/2.0
    return ( xi, yi)


pt1 = (0,9)
pt2 = (1,0)
pt3 = (9,0)
pt4 = (0,1)
print(intersectLines(pt1, pt2, pt3, pt4))
  

lines = []
intersect = []

def original(num, i, w,setcolor):
    for x in range(1,i):
        if num>0:
            plt.plot([0,i-x],[x,0], color=setcolor, linewidth=w)
        if num>1:
            plt.plot([0,i-x],[-x,0], color=setcolor, linewidth=w)
        if num>2:
            plt.plot([0,-(i-x)],[x,0], color=setcolor, linewidth=w)
        if num>3:
            plt.plot([0,-(i-x)],[-x,0], color=setcolor, linewidth=w)

def triinmiddle(num, i, w,setcolor):
    for x in range(1,i):
        if num >0:
            plt.plot([0,i-x],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,x],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,x], color=setcolor,linewidth = w)
        if num >1:
            plt.plot([0,i-x],[-(i-x),-(x)], color=setcolor,linewidth = w)
            plt.plot([0,x],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,-x], color=setcolor,linewidth = w)

        if num >2:
            plt.plot([0,-(i-x)],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,x], color=setcolor,linewidth = w)

        if num >3:
            plt.plot([0,-(i-x)],[-(i-x),-x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,-x], color=setcolor,linewidth = w)

def shape3(num,i,w,setcolor):
    for x in range(1,i):
        if num>0:
            plt.plot([0,i-x],[x,0], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[i-x,0], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[x-1,i-x], color=setcolor, linewidth=w)
        if num>1:
            plt.plot([0,i-x],[-x,0], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[-(i-x),0], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
        if num>2:
            plt.plot([0,-(i-x)],[x,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[i-x,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[x-1,i-x], color=setcolor, linewidth=w)
        if num>3:
            plt.plot([0,-(i-x)],[-x,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[-(i-x),0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)

def shape4 (num, i, w, setcolor):
    for x in range(1,(i//2)+1):
        print(i//2)
        print(x)
        plt.plot([0,x+1],[i-x+1,0])
        plt.plot([0,i-x+1],[i-x-1,x-1])
        plt.plot([x-1,i-x-1],[0,x+1])
        


i = 4
w=0.5
num = 1
setcolor = ('black')
if num>0:
    plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
    plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
if num>1:
    plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
if num>2:
    plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)

#triinmiddle(num,i,w,"red")
#original(num,i,w,"blue")
#shape3(num,i,w,setcolor)
shape4(num,i,w,setcolor)
plt.show() 

