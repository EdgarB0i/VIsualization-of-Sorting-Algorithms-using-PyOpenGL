
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dezone(x, y, zone):
  if zone == 0:
    return x, y
  elif zone == 1:
    return y , x
  elif zone == 2:
    return -y , x
  elif zone == 3:
    return -x , y
  elif zone == 4:
    return -x, -y
  elif zone == 5:
    return -y , -x
  elif zone == 6:
    return y , -x
  elif zone == 7:
    return x , -y
  else:
    print("problem")
    return x , y

def zone_fnc(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  if abs(dx) >= abs(dy) and (dx >= 0 and dy >= 0):
    zone = 0
    return x1, y1, x2, y2, zone
  elif abs(dy) > abs(dx) and (dx >= 0 and dy >= 0):
    zone = 1
    return y1, x1, y2, x2, zone
  elif abs(dy) > abs(dx) and (dx < 0 and dy >= 0):
    zone = 2
    return y1, -x1, y2, -x2, zone
  elif abs(dx) >= abs(dy) and (dx < 0 and dy >= 0):
    zone = 3
    return -x1, y1, -x2, y2, zone
  elif abs(dx) >= abs(dy) and (dx < 0 and dy < 0):
    zone = 4
    return -x1, -y1, -x2, -y2, zone
  elif abs(dy) > abs(dx) and (dx < 0 and dy < 0):
    zone = 5
    return -y1, -x1, -y2, -x2, zone
  elif abs(dy) > abs(dx) and (dx >= 0 and dy < 0):
    zone = 6
    return -y1, x1, -y2, x2, zone
  elif abs(dx) >= abs(dy) and (dx >= 0 and dy < 0):
    zone = 7
    return x1, -y1, x2, -y2, zone

def mid_point(x1, y1, x2, y2):
  zone = 0
  x1 , y1 , x2, y2, zone = zone_fnc(x1, y1, x2, y2)
  dx = x2 - x1
  dy = y2 - y1
  d = 2*dy - dx
  incE = 2*dy
  incNE = 2*(dy-dx)
  y = y1
  x = x1
  glBegin(GL_POINTS)
  while (x<=x2):
    x_t , y_t = dezone(x , y , zone)
    
    glVertex2f(x_t,y_t)
    if (d>0):
      y += 1
      d += incNE
    else:
      d += incE
    x += 1
  glEnd()


def num_display_2(str1, x_start = 0, y_start = 0, size = 100, gap = 20, start = 0):
  dict1 = {"1" : [0, 1, 0 , 0, 0, 0 , 1], 
           "2" : [1, 1, 1 , 0, 1, 1 , 0], 
           "3" : [1, 1, 1 , 0, 0, 1 , 1], 
           "4" : [1, 1, 0 , 1, 0, 0 , 1], 
           "5" : [1, 0, 1 , 1, 0, 1 , 1], 
           "6" : [1, 0, 1 , 1, 1, 1 , 1], 
           "7" : [0, 1, 1 , 0, 0, 0 , 1], 
           "8" : [1, 1, 1 , 1, 1, 1 , 1], 
           "9" : [1, 1, 1 , 1, 0, 1 , 1], 
           "0" : [0, 1, 1 , 1, 1, 1 , 1]}
  list1 = [(0,0,-size,0),
           (0,0,0,size),
           (0,size,-size,size),
           (-size,size,-size,0),
           (-size,0,-size,-size),
           (-size,-size,0, -size),
           (0, -size,0,0)]
  d = 0
  d2 = ((len(str1[start:])-1)*(gap+size)-gap)/2
  for a in str1[start:]:
    i = 0
    while i< len(dict1[a]):
      if dict1[a][i]:
        x1, y1, x2 , y2= list1[i]
        mid_point(x1+d-d2+x_start,y1+y_start,x2+d-d2+x_start,y2+y_start)
      i+=1
    d += gap + size

