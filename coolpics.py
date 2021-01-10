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

def shape4 (num, i, w, setcolor):
    for x in range(1,(i//2)+1):
        if (i-x)==0:
            a = 1
        else:
            a = 0
        if (x+1)<6:
            b = x+1
        else:
            b = x-1
        plt.plot([0,b],[i-x+1,a])
        if (i-x-1)>0:
            c = i-x-1
        else:
            c=x-1
        if (x-1)>3:
            e=0
        else:
            e=x-1
        if (x+1)>5:
            d=0
        else:
            d=x+1
        if (x-1)>3:
            f = x-1
        else:
            f = 0
        plt.plot([e,c],[f,d])
        if (i-x-1<0):
            g=0
        else:
            g=i-x-1
        plt.plot([0,i-x+1],[g,x-1])
        


i = 8
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
