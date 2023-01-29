from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Transformation import *
lst=[]
def mid_circle(x0, y0, r):
  d = 1 - r
  x = 0
  y = r
  while (x<=y):
    #glBegin(GL_POINTS)
    
    #1
    lst.append((x+x0,y+y0))
    #glVertex2f((x + x0), (y + y0))
    #2
    lst.append((y+x0,x+y0))
    #glVertex2f((y+x0),(x+y0))
    #3
    lst.append((-x+x0,-y+y0))
    #glVertex2f((-x+x0),(-y+y0))
    #4  
    lst.append((-y+x0,-x+y0))
    #glVertex2f((-y+x0),(-x+y0))
    #5
    lst.append((-x+x0,y+y0))
    #glVertex2f((-x+x0),(y+y0))
    #6
    lst.append((y+x0,-x+y0))
    #glVertex2f((y+x0),(-x+y0))
    #7
    lst.append((x+x0,-y+y0))
    #glVertex2f((x+x0),(-y+y0))
    #8
    #lst.append((-y+x0,x+y0))
    #glVertex2f((-y+x0),(x+y0))
    
    #glEnd()
    if (d<0):
      d += 2*x+3
    else:
      d += 2*x - 2*y + 5
      y-=1
    x+=1
  

   
