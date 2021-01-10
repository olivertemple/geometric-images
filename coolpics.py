import matplotlib.pyplot as plt
import math

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
plt.show() 

