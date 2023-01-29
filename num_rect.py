from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mid_point_line import *

class rect:
    def __init__(self, sw_x = 0, sw_y = 0, ne_x = 100, ne_y = 100 , num = 888 , color = (0, 0.2, 0.6) , show_num = 1):
        self.sw_x = sw_x
        self.sw_y = sw_y
        self.ne_x = ne_x
        self.ne_y = ne_y
        self.num = num
        self.color = color
        self.show_num = show_num
    
    def draw(self):
        x = self.sw_x
        y = self.sw_y

        glColor3f(self.color[0], self.color[1], self.color[2])
        while x <= self.ne_x:
            mid_point(x, y, x, self.ne_y)
            x+=1
    
        if self.show_num:
            num = str(self.num)

            num_size = (self.ne_x - self.sw_x)/( 3*len(num)/2 + 1)

            x_start = (self.sw_x + self.ne_x) / 2
            y_start = self.sw_y - 3* num_size

            num_display_2(num , size = num_size, gap = num_size/2, x_start = x_start, y_start = y_start)

def list_to_rect_list(list1, gap = 2 , dis_width = 800, dis_height = 600):
    num = len(list1)
    list2 = []
    x_size = (dis_width - gap * (num-1)-50) //num
    max_value = max(list1)
    y_factor = (dis_height-50) * 0.66/ max_value
    sw_x = -dis_width//2 +25
    sw_y = -max_value * y_factor //4
    for a in list1:
        ne_x = x_size + sw_x
        ne_y = y_factor * a + sw_y
        list2.append(rect(sw_x,sw_y,ne_x,ne_y,a))
        sw_x = ne_x+gap
        sw_y = sw_y
    return list2

def rect_copy(r):
    return rect(r.sw_x,r.sw_y,r.ne_x,r.ne_y,r.num,r.color,r.show_num)

def swap_rect_position(rect1 , rect2):
    temp1 = rect_copy(rect1)
    temp2 = rect_copy(rect2)
    if temp1.sw_x < temp2.sw_x:
        fact = 1
    else :
        fact = -1
    while (rect1.sw_x != temp2.sw_x):
        rect1.sw_x += fact*1
        rect1.ne_x += fact*1
        rect2.sw_x -= fact*1
        rect2.ne_x -= fact*1
