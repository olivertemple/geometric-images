import matplotlib.pyplot as plt
import math

def original(num, i, w,setcolor):
    if num>0:
        plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
        plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
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
    if num>0:
        plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
        plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)

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
    if num>0:
        plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
        plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)

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

def threedimensionalshape3(num,i,w,setcolor):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    if num>0:
        ax.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        ax.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        ax.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    if num>1:
        ax.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        ax.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    if num>3:
        ax.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)

    for x in range(1,i):
        if num>0:
            plt.plot([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[i-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[x-1,i-x],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[i-x,0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[x-1,i-x],[i-x,0], color=setcolor, linewidth=w)

            plt.plot([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[0,0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[0,0],[i-x,0], color=setcolor, linewidth=w)

        if num>1:
            plt.plot([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[-(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[-(x-1),-(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(i-x),0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(x-1),-(i-x)],[i-x,0], color=setcolor, linewidth=w)

            plt.plot([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[0,0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[0,0],[i-x,0], color=setcolor, linewidth=w)

        if num>2:
            plt.plot([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[-(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[-(x-1),-(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(i-x),0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(x-1),-(i-x)],[i-x,0], color=setcolor, linewidth=w)

            plt.plot([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[0,0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[0,0],[i-x,0], color=setcolor, linewidth=w)


            plt.plot([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[(x-1),(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[(i-x),0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([0,0],[(x-1),(i-x)],[i-x,0], color=setcolor, linewidth=w)

            plt.plot([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[0,0],[x-1,i-x], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[0,0],[i-x,0], color=setcolor, linewidth=w)
        
        if num>3:
            plt.plot([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[-(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[-(x-1),-(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(i-x),0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(x-1),-(i-x)],[-(i-x),0], color=setcolor, linewidth=w)

            plt.plot([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[0,0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[0,0],[-(i-x),0], color=setcolor, linewidth=w)


            plt.plot([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[(x-1),(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[(i-x),0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[(x-1),(i-x)],[-(i-x),0], color=setcolor, linewidth=w)

            plt.plot([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[0,0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[0,0],[-(i-x),0], color=setcolor, linewidth=w)


            plt.plot([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[-(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[-(x-1),-(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(i-x),0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[-(x-1),-(i-x)],[-(i-x),0], color=setcolor, linewidth=w)

            plt.plot([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[0,0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[0,0],[-(i-x),0], color=setcolor, linewidth=w)


            plt.plot([0,(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([(x-1),(i-x)],[(i-x),0],[0,0], color=setcolor, linewidth=w)
            plt.plot([(i-x),0],[(x-1),(i-x)],[0,0], color=setcolor, linewidth=w)

            plt.plot([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[(i-x),0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([0,0],[(x-1),(i-x)],[-(i-x),0], color=setcolor, linewidth=w)

            plt.plot([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([(i-x),0],[0,0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
            plt.plot([(x-1),(i-x)],[0,0],[-(i-x),0], color=setcolor, linewidth=w)


def threedimensionaloriginal(num,i,w,setcolor):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    if num>0:
        ax.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        ax.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        ax.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    if num>1:
        ax.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        ax.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    if num>3:
        ax.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)

    for x in range(1,i):
        if num >0:
            ax.plot3D([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            ax.plot3D([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
        if num>1:
            ax.plot3D([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            ax.plot3D([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)

        if num>2: 
            ax.plot3D([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            ax.plot3D([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
            ax.plot3D([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            ax.plot3D([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)

        if num>3:
            ax.plot3D([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            ax.plot3D([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            ax.plot3D([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            ax.plot3D([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            ax.plot3D([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            ax.plot3D([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            ax.plot3D([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            ax.plot3D([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            ax.plot3D([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

def threedimensionaltriinmiddle(num,i,w,setcolor):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    if num>0:
        ax.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        ax.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        ax.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    if num>1:
        ax.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        ax.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    if num>3:
        ax.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)
    
    for x in range(1,i):
        if num>0:
            ax.plot([0,i-x],[i-x,x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,x],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[i-x,x],[0,i-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[i-x,0],[0,x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,x],[x,i-x], color=setcolor,linewidth = w)

            ax.plot([0,i-x],[0,0],[i-x,x], color=setcolor,linewidth = w)
            ax.plot([0,x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,0],[0,x], color=setcolor,linewidth = w)

        if num>1:
            ax.plot([0,i-x],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,-(x)],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[-(i-x),-x],[0,i-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[-(i-x),0],[0,x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,-x],[x,i-x], color=setcolor,linewidth = w)

            ax.plot([0,i-x],[0,0],[i-x,x], color=setcolor,linewidth = w)
            ax.plot([0,x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,0],[0,x], color=setcolor,linewidth = w)

        if num>2:
            ax.plot([0,-(i-x)],[i-x,x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,-x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,x],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[i-x,x],[0,i-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[i-x,0],[0,x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,x],[x,i-x], color=setcolor,linewidth = w)

            ax.plot([0,-(i-x)],[0,0],[i-x,x], color=setcolor,linewidth = w)
            ax.plot([0,-x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,0],[0,x], color=setcolor,linewidth = w)
            
            ax.plot([0,-(i-x)],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,-x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,-x],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[-(i-x),-x],[0,i-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[-(i-x),0],[0,x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,-x],[x,i-x], color=setcolor,linewidth = w)

            ax.plot([0,-(i-x)],[0,0],[i-x,x], color=setcolor,linewidth = w)
            ax.plot([0,-x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,0],[0,x], color=setcolor,linewidth = w)

        if num>3:
            ax.plot([0,i-x],[i-x,x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,x],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[i-x,x],[0,-(i-x)], color=setcolor,linewidth = w)
            ax.plot([0,0],[i-x,0],[0,-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,x],[-x,-(i-x)], color=setcolor,linewidth = w)

            ax.plot([0,i-x],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            ax.plot([0,x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,0],[0,-x], color=setcolor,linewidth = w)

            ax.plot([0,i-x],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,-(x)],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[-(i-x),-x],[0,-(i-x)], color=setcolor,linewidth = w)
            ax.plot([0,0],[-(i-x),0],[0,-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,-x],[-x,-(i-x)], color=setcolor,linewidth = w)

            ax.plot([0,i-x],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            ax.plot([0,x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            ax.plot([x,i-x],[0,0],[0,-x], color=setcolor,linewidth = w)

            ax.plot([0,-(i-x)],[i-x,x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,-x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,x],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[i-x,x],[0,-(i-x)], color=setcolor,linewidth = w)
            ax.plot([0,0],[i-x,0],[0,-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,x],[-x,-(i-x)], color=setcolor,linewidth = w)

            ax.plot([0,-(i-x)],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            ax.plot([0,-x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,0],[0,-x], color=setcolor,linewidth = w)

            
            ax.plot([0,-(i-x)],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            ax.plot([0,-x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,-x],[0,0], color=setcolor,linewidth = w)

            ax.plot([0,0],[-(i-x),-x],[0,-(i-x)], color=setcolor,linewidth = w)
            ax.plot([0,0],[-(i-x),0],[0,-x], color=setcolor,linewidth = w)
            ax.plot([0,0],[0,-x],[-x,-(i-x)], color=setcolor,linewidth = w)

            ax.plot([0,-(i-x)],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            ax.plot([0,-x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            ax.plot([-x,-(i-x)],[0,0],[0,-x], color=setcolor,linewidth = w)


        

i = 20
w=0.5
num = 4
setcolor = ('black')


#triinmiddle(num,i,w,"red")
#original(num,i,w,"blue")
#shape3(num,i,w,setcolor)
#threedimensionaloriginal(num,i,w,setcolor)
#threedimensionaltriinmiddle(num,i,w,setcolor)
threedimensionalshape3(num,i,w,setcolor)
plt.show() 

