from tealight.art import (color, line, spot, circle, box, image, text, background)
from github.andyandywells.art.matrixFunctions import *
from github.griffithsben.art.connect4_defs import *


matrix = initialiseMatrix()

Pturn = 1
def handle_mousedown(x,y):
  global Pturn
  Array_X = (x - offset_x) // cell_size
  Array_Y = (y - offset_y) // cell_size
  if(Array_X >=7 or Array_X <0 or Array_Y <0  or Array_Y >= 7):
    return 0
    
  CentreX = (Array_X+1)*100+75
  CentreY = (2+Array_Y)*100 +50  
  if (Pturn == 1): 
    color("red")
    Pturn = -1 
  else:
    color("yellow")
    Pturn = 1
    
  if(CentreX != 0):         
    if (matrix[Array_X][Array_Y] == 0):
        
      spot(CentreX-1,CentreY-1, 35)
      matrix[Array_X][Array_Y] = Pturn
      print matrix
      
         
       
        
  
  print(checkwin(matrix))
 
  
  print(checkwin(matrix))
 
