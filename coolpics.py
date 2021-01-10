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

def threedimensionaloriginal(num,i,w,setcolor,ax):
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
            plt.plot([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
        if num>1:
            plt.plot([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)

        if num>2: 
            plt.plot([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
            plt.plot([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)

        if num>3:
            plt.plot([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            plt.plot([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            plt.plot([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

            plt.plot([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[-x,0],[0,-(i-x)], color=setcolor, linewidth=w)
            plt.plot([-x,0],[0,0],[0,-(i-x)], color=setcolor, linewidth=w)

def threedimensionaltriinmiddle(num,i,w,setcolor,ax):
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
parser.add_argument('-dimensions', type=int,default=2, help='2D/3D output image (2 for 2D, 3 for 3D).')
parser.add_argument('-i',type=int, default=20, help='Size of output image.')
parser.add_argument('-w', type=float, default = 0.5, help='Width of line, recommended less than 1.')
parser.add_argument('-num',type=int, default=4,help='How many quadrants to be filled, 1-4.')
parser.add_argument('-shape',type=int, default=1, help='Shape 1 number (1-3).')
parser.add_argument('-shape2',type=int, default=0, help='Shape 2 number (optional)(1-3).')
parser.add_argument('-setcolour', help='Colour of shape 1.')
parser.add_argument('-setcolour2', help='Colour of shape 2.')
args = parser.parse_args()

i = args.i
w=args.w
num = args.num
dim = args.dimensions
setcolor = args.setcolour
setcolor2 = args.setcolour2


if dim==2:
    if args.shape==1:
        original(num,i,w,setcolor)
    elif args.shape==2:
        triinmiddle(num,i,w,setcolor)
    elif args.shape==3:
        shape3(num,i,w,setcolor)
    if args.shape2 > 0:
        if args.shape2==1:
            original(num,i,w,setcolor2)
        elif args.shape2==2:
            triinmiddle(num,i,w,setcolor2)
        elif args.shape2==3:
            shape3(num,i,w,setcolor2)

else:   
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    if args.shape==1:
        threedimensionaloriginal(num,i,w,setcolor,ax)
    elif args.shape==2:
        threedimensionaltriinmiddle(num,i,w,setcolor,ax)
    elif args.shape==3:
        threedimensionalshape3(num,i,w,setcolor,ax)
    if args.shape2 > 0:
        if args.shape2==1:
            threedimensionaloriginal(num,i,w,setcolor2,ax)
        elif args.shape2==2:
            threedimensionaltriinmiddle(num,i,w,setcolor2,ax)
        elif args.shape2==3:
            threedimensionalshape3(num,i,w,setcolor2,ax)


plt.savefig(str(args.dimensions) + 'D, ' + str(args.i)+' ,'+str(args.shape))
plt.show() 
