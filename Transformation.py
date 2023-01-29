from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math
import time
def rotate(theta,x,y):
    cosT=math.cos(theta)
    sinT=math.sin(theta)
    result=[[0],[0]]
    A=[[cosT,sinT],
    [-sinT,cosT]]
    B=[[x],[y]]
    result = np.dot(A,B)
    a=result[0]
    b=result[1]
    return(a[0],b[0])

def scaling(k_x, k_y, x, y):
    result=[[0],[0]]
    A=[[k_x,0],
    [0,k_y]]
    B=[[x],[y]]
    result = np.dot(A,B)
    a=result[0]
    b=result[1]
    return(a[0],b[0])

def translate(x,y,move_x=0,move_y=0):
    glBegin(GL_POINTS)
    glVertex2f(x+move_x,y+move_y)
    glEnd()
    
    
