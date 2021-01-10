import matplotlib.pyplot as plt
import math
import argparse

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

def threedimensionaloriginal(num,i,w,setcolor):
    ax = plt.axes(projection='3d')
    if num>0:
        plt.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        plt.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        plt.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    if num>3:
        plt.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)

    for x in range(1,i):
        if num >0:
            plt.plot3D([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot3D([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
        if num>1:
            plt.plot3D([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot3D([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)

        if num>2: 
            plt.plot3D([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot3D([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
            plt.plot3D([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot3D([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)

        if num>3:
            plt.plot3D([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot3D([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            plt.plot3D([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot3D([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            plt.plot3D([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot3D([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            plt.plot3D([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot3D([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot3D([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

def threedimensionaltriinmiddle(num,i,w,setcolor,ax):
    ax = plt.axes(projection='3d')
    if num>0:
        plt.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        plt.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        plt.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    if num>3:
        plt.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)
    
    for x in range(1,i):
        if num>0:
            plt.plot([0,i-x],[i-x,x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,x],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[i-x,x],[0,i-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[i-x,0],[0,x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,x],[x,i-x], color=setcolor,linewidth = w)

            plt.plot([0,i-x],[0,0],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,0],[0,x], color=setcolor,linewidth = w)

        if num>1:
            plt.plot([0,i-x],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,-(x)],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[-(i-x),-x],[0,i-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[-(i-x),0],[0,x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,-x],[x,i-x], color=setcolor,linewidth = w)

            plt.plot([0,i-x],[0,0],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,0],[0,x], color=setcolor,linewidth = w)

        if num>2:
            plt.plot([0,-(i-x)],[i-x,x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,-x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,x],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[i-x,x],[0,i-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[i-x,0],[0,x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,x],[x,i-x], color=setcolor,linewidth = w)

            plt.plot([0,-(i-x)],[0,0],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,0],[0,x], color=setcolor,linewidth = w)
            
            plt.plot([0,-(i-x)],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,-x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,-x],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[-(i-x),-x],[0,i-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[-(i-x),0],[0,x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,-x],[x,i-x], color=setcolor,linewidth = w)

            plt.plot([0,-(i-x)],[0,0],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[0,0],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,0],[0,x], color=setcolor,linewidth = w)

        if num>3:
            plt.plot([0,i-x],[i-x,x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,x],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[i-x,x],[0,-(i-x)], color=setcolor,linewidth = w)
            plt.plot([0,0],[i-x,0],[0,-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,x],[-x,-(i-x)], color=setcolor,linewidth = w)

            plt.plot([0,i-x],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            plt.plot([0,x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,0],[0,-x], color=setcolor,linewidth = w)

            plt.plot([0,i-x],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,-(x)],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[-(i-x),-x],[0,-(i-x)], color=setcolor,linewidth = w)
            plt.plot([0,0],[-(i-x),0],[0,-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,-x],[-x,-(i-x)], color=setcolor,linewidth = w)

            plt.plot([0,i-x],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            plt.plot([0,x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,0],[0,-x], color=setcolor,linewidth = w)

            plt.plot([0,-(i-x)],[i-x,x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,-x],[i-x,0],[0,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,x],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[i-x,x],[0,-(i-x)], color=setcolor,linewidth = w)
            plt.plot([0,0],[i-x,0],[0,-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,x],[-x,-(i-x)], color=setcolor,linewidth = w)

            plt.plot([0,-(i-x)],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,0],[0,-x], color=setcolor,linewidth = w)

            
            plt.plot([0,-(i-x)],[-(i-x),-x],[0,0], color=setcolor,linewidth = w)
            plt.plot([0,-x],[-(i-x),0],[0,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,-x],[0,0], color=setcolor,linewidth = w)

            plt.plot([0,0],[-(i-x),-x],[0,-(i-x)], color=setcolor,linewidth = w)
            plt.plot([0,0],[-(i-x),0],[0,-x], color=setcolor,linewidth = w)
            plt.plot([0,0],[0,-x],[-x,-(i-x)], color=setcolor,linewidth = w)

            plt.plot([0,-(i-x)],[0,0],[-(i-x),-x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[0,0],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,0],[0,-x], color=setcolor,linewidth = w)

def threedimensionalshape3(num,i,w,setcolor,ax):
    if num>0:
        plt.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        plt.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        plt.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    if num>3:
        plt.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)

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

parser = argparse.ArgumentParser(description = 'Draw geometric Images.')
parser.add_argument('-dimensions', type=int)
parser.add_argument('-num',type=int)
parser.add_argument('-shape',type=int)
#parser.add_argument('-setcolor',type=input)
args = parser.parse_args()




i = 20
w=0.5
num = args.num
setcolor = ('black')
dim = args.dimensions

if dim==2:
    if args.shape==1:
        original(num,i,w,"blue")
    if args.shape==2:
        triinmiddle(num,i,w,"red")
    if args.shape==3:
        shape3(num,i,w,setcolor)

else:   
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    if args.shape==1:
        threedimensionaloriginal(num,i,w,setcolor)
    if args.shape==2:
        threedimensionaltriinmiddle(num,i,w,'red',ax)
    if args.shape==3:
        threedimensionalshape3(num,i,w,setcolor,ax)
plt.show() 

