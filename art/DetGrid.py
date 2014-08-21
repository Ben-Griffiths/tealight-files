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
    if(CentreX != 0):         
      
    #  matrix[Array_X][Array_Y] = Pturn
      print matrix
      color("red")
      Pturn = -1    
  else:
    if(CentreX != 0):        
    #  matrix[Array_X][Array_Y] = Pturn
      print matrix
      color("yellow")
      Pturn = 1
      
  


     
  for i in range (0,6):
    if matrix[i][Array_X] == 1 or matrix[i][Array_X] == -1:
      Array_Y = i-1
      matrix[Array_Y][Array_X] = Pturn      
      CentreX = (Array_X+1)*100+75
      CentreY = (2+Array_Y)*100 +50  
      spot(CentreX-1,CentreY-1, 35)
      return 0
    else:
      if (matrix[6][Array_X] != 0):
        Array_Y = 6 
        CentreX = (Array_X+1)*100+75
        CentreY = (2+Array_Y)*100 +50  
        spot(CentreX-1,CentreY-1, 35)
   
  
  
  # print (CentreX,CentreY,Array_X,Array_Y)
  
#if (gridarray[i,j-1] != 0):
#  update colour and array
#else
#  set up a goto
