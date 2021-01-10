###Geometric Images###
#Programming by Oliver Temple
#https://github.com/olivertemple/geometric-images
import matplotlib.pyplot as plt
import math
import argparse

def original(num, i, w,setcolor): #original shape
    #one quadrant
    if num>0:
        plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
        plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
    #two quadrants
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    #three/four quadrants
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    #repeats for the value of i(length of the axis)
    for x in range(1,i):
        #one quadrant
        if num>0:
            plt.plot([0,i-x],[x,0], color=setcolor, linewidth=w)
        #two quadrants
        if num>1:
            plt.plot([0,i-x],[-x,0], color=setcolor, linewidth=w)
        #three quadrants
        if num>2:
            plt.plot([0,-(i-x)],[x,0], color=setcolor, linewidth=w)
        #four quadrants
        if num>3:
            plt.plot([0,-(i-x)],[-x,0], color=setcolor, linewidth=w)

def triinmiddle(num, i, w,setcolor):#2nd shape
    #one quadrant
    if num>0:
        plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
        plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
    #two quadrants
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    #three/four quadrants
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)

    #repeats for the value of i(length of the axis)
    for x in range(1,i):
        #one quadrant
        if num >0:
            plt.plot([0,i-x],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,x],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,x], color=setcolor,linewidth = w)
        #two quadrants
        if num >1:
            plt.plot([0,i-x],[-(i-x),-(x)], color=setcolor,linewidth = w)
            plt.plot([0,x],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([x,i-x],[0,-x], color=setcolor,linewidth = w)
        #three quadrants
        if num >2:
            plt.plot([0,-(i-x)],[i-x,x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[i-x,0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,x], color=setcolor,linewidth = w)
        #four quadrants
        if num >3:
            plt.plot([0,-(i-x)],[-(i-x),-x], color=setcolor,linewidth = w)
            plt.plot([0,-x],[-(i-x),0], color=setcolor,linewidth = w)
            plt.plot([-x,-(i-x)],[0,-x], color=setcolor,linewidth = w)

def shape3(num,i,w,setcolor):#3rd shape
    #one quadrant
    if num>0:
        plt.plot([0,0],[0,i-1],color=setcolor, linewidth=w)
        plt.plot([0,i-1],[0,0],color=setcolor, linewidth=w)
    #two quadrants
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    #three quadrants
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)

    #repeats for the value of i(length of the axis)
    for x in range(1,i):
        #one quadrant
        if num>0:
            plt.plot([0,i-x],[x,0], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[i-x,0], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[x-1,i-x], color=setcolor, linewidth=w)
        #two quadrants
        if num>1:
            plt.plot([0,i-x],[-x,0], color=setcolor, linewidth=w)
            plt.plot([x-1,i-x],[-(i-x),0], color=setcolor, linewidth=w)
            plt.plot([i-x,0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)
        #three quadrants
        if num>2:
            plt.plot([0,-(i-x)],[x,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[i-x,0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[x-1,i-x], color=setcolor, linewidth=w)
        #four quadrants
        if num>3:
            plt.plot([0,-(i-x)],[-x,0], color=setcolor, linewidth=w)
            plt.plot([-(x-1),-(i-x)],[-(i-x),0], color=setcolor, linewidth=w)
            plt.plot([-(i-x),0],[-(x-1),-(i-x)], color=setcolor, linewidth=w)

def threedimensionaloriginal(num,i,w,setcolor,ax):#3D version of original shape
    #one quadrant
    if num>0:
        plt.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        plt.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        plt.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    #two quadrants
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    #three quadrants
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    #four quadrants
    if num>3:
        plt.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)

    #repeats for the value of i(length of the axis)
    for x in range(1,i):
        #one quadrant
        if num >0:
            plt.plot([0,i-x],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        #two quadrants
        if num>1:
            plt.plot([0,i-x],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        #four quadrants
        if num>2: 
            plt.plot([0,-(i-x)],[x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        
            plt.plot([0,-(i-x)],[-x,0],[0,0], color=setcolor, linewidth=w)
            plt.plot([0,0],[-x,0],[0,i-x], color=setcolor, linewidth=w)
            plt.plot([-x,0],[0,0],[0,i-x], color=setcolor, linewidth=w)
        #eight quadrants
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

def threedimensionaltriinmiddle(num,i,w,setcolor,ax):#3D version of 2nd shape
    #one quadrant
    if num>0:
        plt.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        plt.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        plt.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    #two quadrants
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    #three quadrants
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    #four quadrants
    if num>3:
        plt.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)
    
    #repeats for the value of i(length of the axis)
    for x in range(1,i):
        #one quadrant
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
        #two quadrants
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
        #three quadrants
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
        #four quadrants
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

def threedimensionalshape3(num,i,w,setcolor,ax):#3D version of the 3rd shape
    #one quadrant
    if num>0:
        plt.plot([0,0,0],[0,i-1,0],color=setcolor, linewidth=w)
        plt.plot([0,0],[0,0],[0,i-1],color=setcolor, linewidth=w)        
        plt.plot([0,i-1,0],[0,0,0],color=setcolor, linewidth=w)
    #two quadrants
    if num>1:
        plt.plot([0,0],[0,-i+1],color=setcolor, linewidth=w)
    #three quadrants
    if num>2:
        plt.plot([0,-i+1],[0,0],color=setcolor, linewidth=w)
    #four quadrants
    if num>3:
        plt.plot([0,0],[0,0],[0,-(i-1)],color=setcolor, linewidth=w)
    
    #repeats for the value of i(length of the axis)
    for x in range(1,i):
        #one quadrant
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
        #two quadrants
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
        #three quadrants
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
        #four quadrants
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

#parses arguments from the command line to the program
parser = argparse.ArgumentParser(description = 'Draw geometric Images.')
#dimensions of the output (2D/3D)
parser.add_argument('-dimensions', type=int,default=2, help='2D/3D output image (2 for 2D, 3 for 3D).')
#Size of the image
parser.add_argument('-i',type=int, default=20, help='Size of output image.')
#width of the line
parser.add_argument('-w', type=float, default = 0.5, help='Width of line, recommended less than 1.')
#number of quadrants to be filled
parser.add_argument('-num',type=int, default=4,help='How many quadrants to be filled, 1-4.')
#1st shape
parser.add_argument('-shape',type=int, default=1, help='Shape 1 number (1-3).')
#2nd shape (optional)
parser.add_argument('-shape2',type=int, default=0, help='Shape 2 number (optional)(1-3).')
#colour of the first shape
parser.add_argument('-colour', help='Colour of shape 1, either as a word, hex or RGB')
#colour of the second shape
parser.add_argument('-colour2', help='Colour of shape 2, either as a word, hex or RGB')
args = parser.parse_args()

i = args.i
w=args.w
num = args.num
dim = args.dimensions
setcolor = args.colour
setcolor2 = args.colour2

#two dimensions
if dim==2:
    #1st shape
    if args.shape==1:
        original(num,i,w,setcolor)
    elif args.shape==2:
        triinmiddle(num,i,w,setcolor)
    elif args.shape==3:
        shape3(num,i,w,setcolor)
    #second shape if argument is given
    if args.shape2 > 0:
        if args.shape2==1:
            original(num,i,w,setcolor2)
        elif args.shape2==2:
            triinmiddle(num,i,w,setcolor2)
        elif args.shape2==3:
            shape3(num,i,w,setcolor2)

#three dimensions
else: 
    #creates 3D axis
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    #1st shape
    if args.shape==1:
        threedimensionaloriginal(num,i,w,setcolor,ax)
    elif args.shape==2:
        threedimensionaltriinmiddle(num,i,w,setcolor,ax)
    elif args.shape==3:
        threedimensionalshape3(num,i,w,setcolor,ax)
    #2nd shape if argument is given
    if args.shape2 > 0:
        if args.shape2==1:
            threedimensionaloriginal(num,i,w,setcolor2,ax)
        elif args.shape2==2:
            threedimensionaltriinmiddle(num,i,w,setcolor2,ax)
        elif args.shape2==3:
            threedimensionalshape3(num,i,w,setcolor2,ax)

#saves the output
plt.savefig(str(args.dimensions) + 'D, ' + str(args.i)+' ,'+str(args.shape))
#shows the outputs
plt.show() 
