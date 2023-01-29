from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mid_point_line import *
from mid_point_circle import *
from num_rect import *
import time
from Transformation import *

WIDTH = 800
HEIGHT = 600



a = [10,60,50,30,28,45,69,10,25]
b = list_to_rect_list(a)
swap_list = [(1,2),(1,3),(0,1)]

swap_going = 0

mem = [0,0,0]
target1 = b[1]
target2 = b[2]
target1_x = target1.sw_x
target2_x = target2.sw_x
s = 5

def connector(list1, s_going = 1, s_list = [], speed = 10):
    global b , target1, target1_x, target2, target2_x, s , swap_list, swap_going
    swap_list = s_list
    b = list1
    s = speed
    swap_going = s_going
    b[swap_list[0][0]] ,b[swap_list[0][1]] = swap_rect(b[swap_list[0][0]] ,b[swap_list[0][1]])
    print(swap_list.pop(0))
    main_loop()

def iterate():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-WIDTH//2, WIDTH//2, -HEIGHT//2, HEIGHT//2, 0.0, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def swap_rect(rect1 , rect2):
    global target1, target2, swap_going, target1_x, target2_x
    target1 = rect1
    target2 = rect2
    target1.color = (0.8,0,0.8)
    target2.color = (0, 0.8, 0)
    target1_x = rect1.sw_x
    target2_x = rect2.sw_x
    swap_going = 1
    return rect2 , rect1

#------------------------------Global variables for circles------------------
count = 0
k_x , k_y = 0.995,0.995
c = -1
#---------------------------------------------------------------------------


def showScreen():
    global target1, target2, swap_going , target1_x, target2_x,b,s
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here

    glPointSize(1)
    if swap_going:

        if target1_x < target2_x:
            fact = 1
            bol = 1
        else :
            bol = 0
            fact = -1
        target1.sw_x += fact*s
        target1.ne_x += fact*s
        target2.sw_x -= fact*s
        target2.ne_x -= fact*s

        if bol and target1.sw_x >= target2_x :
            if len(swap_list):
                target1.color = (0, 0.2, 0.6)
                target2.color = (0, 0.2, 0.6)
                b[swap_list[0][0]] ,b[swap_list[0][1]] = swap_rect(b[swap_list[0][0]] ,b[swap_list[0][1]])
                swap_list.pop(0)
            else:
                swap_going = 0
            
        elif not(bol) and target1.sw_x <= target2_x:
            if len(swap_list):
                target1.color = (0, 0.2, 0.6)
                target2.color = (0, 0.2, 0.6)
                b[swap_list[0][0]] ,b[swap_list[0][1]] = swap_rect(b[swap_list[0][0]] ,b[swap_list[0][1]])
                swap_list.pop(0)
                
            else:
                swap_going = 0
        

    for i in b:
      i.draw()
    target1.draw()
    target2.draw()
    

    #----------------------------------------------for circles/visuals------------------------------------------------
    i = 0
    global lst , count, k_x , k_y,c
    while i < len(lst):
        x , y = lst[i][0], lst[i][1]
        lst[i] = rotate(math.pi/30, x, y)

        x , y = lst[i][0], lst[i][1]
        if count == 40:
            c = c*(-1)
            k_x = k_x + 0.010 * c
            k_y = k_y + 0.010 * c
            count = 0
        lst[i] = scaling(k_x,k_y, x, y)

        translate(x, y, move_x=240, move_y = -180)
        i+=1
    count+=1
    #--------------------------------------line/character visuals--------------------------------------
    #S
    mid_point(200,-230,200,-220)
    mid_point(200,-220,210,-220)
    mid_point(200,-230,208,-230)
    mid_point(208,-230,208,-240)
    mid_point(208,-240,200,-240)
    #O
    mid_point(220,-220,230,-220)
    mid_point(220,-220,220,-240)
    mid_point(220,-240,230,-240)
    mid_point(230,-220,230,-240)
    #R
    mid_point(240,-220,240,-240)
    mid_point(240,-220,250,-220)
    mid_point(250,-220,250,-230)
    mid_point(240,-230,250,-230)
    mid_point(240,-230,250,-240)
    #T
    mid_point(260,-220,270,-220)
    mid_point(265,-220,265,-240)
    #I
    mid_point(280,-220,280,-240)
    #N
    mid_point(290,-220,290,-240)
    mid_point(290,-220,300,-240)
    mid_point(300,-220,300,-240)
    #G
    mid_point(310,-220,310,-240)
    mid_point(310,-220,323,-220)
    mid_point(310,-240,320,-240)
    mid_point(320,-230,320,-240)
    mid_point(320,-230,328,-230)
    mid_point(328,-230,328,-240)
    #.
    mid_point(335,-240,335,-240)
    mid_point(343,-240,343,-240)
    mid_point(351,-240,351,-240)
    mid_point(359,-240,359,-240)

    #---------------------------------------------------------------------------------------------------

    glutPostRedisplay()
    glutSwapBuffers()



def main_loop():
    mid_circle(0, 0, 25) #circles
    mid_circle(0, 0, 22) #circles
    
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT) #window size
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"Sorting Visualizer") #window nam

    glutDisplayFunc(showScreen)


    glutMainLoop()