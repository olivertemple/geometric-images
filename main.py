###Geometric Images###
#Programming by Oliver Temple
#https://github.com/olivertemple/geometric-images
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import math
import argparse
import PySimpleGUI as sg


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

def threedimensionaloriginal(num,i,w,setcolor):#3D version of original shape
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

def threedimensionaltriinmiddle(num,i,w,setcolor):#3D version of 2nd shape
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

def threedimensionalshape3(num,i,w,setcolor):#3D version of the 3rd shape
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
#if dim==2:
#    plt.figure()
    #1st shape
#    if args.shape==1:
#        original(num,i,w,setcolor)
#    elif args.shape==2:
#        triinmiddle(num,i,w,setcolor)
#    elif args.shape==3:
#        shape3(num,i,w,setcolor)
    #second shape if argument is given
#    if args.shape2 > 0:
#        if args.shape2==1:
#            original(num,i,w,setcolor2)
#        elif args.shape2==2:
#            triinmiddle(num,i,w,setcolor2)
 #       elif args.shape2==3:
 #           shape3(num,i,w,setcolor2)

#three dimensions
#else: 
    #creates 3D axis
 #   fig = plt.figure()
 #   ax = plt.axes(projection='3d')
 #   #1st shape
 #   if args.shape==1:
 #       threedimensionaloriginal(num,i,w,setcolor,ax)
 #   elif args.shape==2:
 #       threedimensionaltriinmiddle(num,i,w,setcolor,ax)
 #   elif args.shape==3:
 #       threedimensionalshape3(num,i,w,setcolor,ax)
    #2nd shape if argument is given
 #   if args.shape2 > 0:
  #          threedimensionaloriginal(num,i,w,setcolor2,ax)
 ##       if args.shape2==1:
 #       elif args.shape2==2:
 #           threedimensionaltriinmiddle(num,i,w,setcolor2,ax)
 #       elif args.shape2==3:
 #           threedimensionalshape3(num,i,w,setcolor2,ax)

#saves the output
#plt.savefig(str(args.dimensions) + 'D, ' + str(args.i)+' ,'+str(args.shape))
#shows the outputs
#plt.show() 



def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right',fill='both',expand=1)

class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args,**kwargs)


menu_def = [['&file',['&save    Ctrl-S']]]

layout = [
[sg.Text("Geometrical shape generator")],
[sg.Text("This program will generate either 2D or 3D geometrical shapes, depending on your input.")],
[sg.Menu(menu_def)],
[sg.Button("1",image_filename="./outputs/2D, 20 ,1.png", image_subsample=2, key='original'), sg.Button("2",image_filename="./outputs/2D, 20 ,2.png", image_subsample=2,key='triinmiddle'), sg.Button("3",image_filename="./outputs/2D, 20 ,3.png", image_subsample=2, key='shape3')],
[sg.Checkbox('Dimensions, Tick for 3D, leave for 2D', default=False, auto_size_text=True, key='dim')],
[sg.Text(text='The Shape being Plotted:\n',key='text_box', size = (100,2),pad=(0,0))],
[sg.Text(text="Colour, in either Hex (#AABBCC), RGB(255,255,255) or as a word (red):",pad=(0,0)),sg.Input(default_text='black', key='setcolor')],
[sg.Text(text='Size of image:',pad=(0,0)),sg.Input(default_text='20', key='i', size = (5,10)), sg.Text(text="Number of quadrants(1-4):", pad=(0,0)), sg.Input(default_text="4", key="num", size=(5,10)), sg.Text(text="Width of lines (only needs adjusting for large sizes", pad=(0,0)),sg.Input(default_text="0.5", key = 'w', size = (5,10))],
[sg.Button("Plot"),sg.Button("Reset")],
[sg.Canvas(key='fig_cv', size=(550,550))],
[sg.Canvas(key='controls_cv')]
]

window= sg.Window("Geometrical Shape Generator", layout, resizable=True).finalize()
window.Maximize()

shape = 1
string = 'The Shape being Plotted:\n'
d2 = False
d3 = False
while True:
    event, values = window.read()
    if event=='Close' or event == sg.WIN_CLOSED:
        break
    if event=='original':
        shape=1
    elif event=='triinmiddle':
        shape=2
    elif event=='shape3':
        shape = 3

    if values['dim']==True:
        dim = 3
        if d3 == False:
            ax = plt.axes(projection='3d')
            string = 'The Shape being Plotted:\n'
            window.Element('text_box').update(string)
        d3 = True
        d2 = False
    elif values['dim']==False:
        dim = 2
        if d2 == False:
            ax = plt.axes()
            string = 'The Shape being Plotted:\n'
            window.Element('text_box').update(string)
        d2 = True
        d3 = False
    if event == 'Reset':
        string = 'The Shape being Plotted:\n'
        window.Element('text_box').update(string)
        if dim == 2:
            plt.cla()
            plt.figure(1)
            fig = plt.gcf()
            DPI=fig.get_dpi()
            fig.set_size_inches(404*2/float(DPI),404/float(DPI))
            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        elif dim==3:
            plt.cla()
            plt.figure(1)
            fig = plt.gcf()
            DPI=fig.get_dpi()
            fig.set_size_inches(404*2/float(DPI),404/float(DPI))
            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
    else:
        window.Element('text_box').update(string+' Shape' + str(shape)+', '+str(dim)+'D.')

    if event == 'Plot': 
        string += (' Shape' + str(shape)+', '+str(dim)+'D.')
        window.Element('text_box').update(string)      
        setcolor = (values['setcolor'])
        i = int(values["i"])
        num = int(values["num"])
        w = float(values['w'])
        if dim == 2:
            #ax = plt.axes()
            if shape == 1:
                original(num, i, w, setcolor)
            elif shape==2:
                triinmiddle(num, i, w, setcolor)
            elif shape==3:
                shape3(num, i, w,setcolor)
        elif dim==3:
            #ax = plt.axes(projection='3d')
            if shape == 1:
                threedimensionaloriginal(num, i, w, setcolor)
            elif shape==2:
                threedimensionaltriinmiddle(num, i, w, setcolor)
            elif shape==2:
                threedimensionalshape3(num, i, w , setcolor)

        plt.figure(1)
        fig = plt.gcf()
        DPI=fig.get_dpi()

        fig.set_size_inches(404*2/float(DPI),404/float(DPI))
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)














