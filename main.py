from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mid_point_line import *
from mid_point_circle import *
from num_rect import *
import opengl_screen as ogls

a = [381,419,495,191,356,355,842,306,964,495,191,356,565,964,495,191,356,355,842,306,936,565,840,740,243,621,608,964,400,897,349,335,824,720,439,710,390]
b = list_to_rect_list(a)
swap_list = [(0,0)]

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        swap_list.append((j,j+1))
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        swap_list.append((step,min_idx))
        (array[step], array[min_idx]) = (array[min_idx], array[step])

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                swap_list.append((j+1,j))
                j -= 1
        
        arr[j + 1] = key

def merge(arr, start, mid, end):
    start2 = mid + 1
  
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
  
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
  
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1
            # element 2, right by 1.
            i = 0
            while (index != start):
                swap_list.append((start2-i,start2-i-1))
                arr[index] = arr[index - 1]
                index -= 1
                i+=1
  
            arr[start] = value
  
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
    
def mergeSort(arr, l, r):
    if (l < r):
  
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
  
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
  
        merge(arr, l, m, r)


#Taking input from the user to visualize the algortihm
inpt=input("Enter the name of the algorithm you want to visualize: ")
inpt=inpt.lower()

if inpt=='bubble':
  bubbleSort(a)

elif inpt=="selection":
  selectionSort(a, len(a))

elif inpt=="insertion":
  insertionSort(a)

elif inpt=="merge":
  mergeSort(a, 0, len(a)-1)


print(a)
print(swap_list)
ogls.connector(b, s_list=swap_list, speed = 5)