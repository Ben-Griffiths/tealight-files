from tealight.art import (color, line, spot, circle, box, image, text, background)
from github.andyandywells.matrixFunctions import *
from github.griffithsben.art.connect4_defs import *

matrix = initialiseMatrix()

Pturn = True
def handle_mousedown(x,y):
  global Pturn
  Array_X = (x - offset_x) // cell_size
  Array_Y = (y - offset_y) // cell_size
  CentreX = (Array_X+1)*100+75
  CentreY = (2+Array_Y)*100 +50
  print matrix
  if (Pturn == True):
    Pturn = False
    if(CentreX != 0):         
      Pturn = False
      color("red")
          
  else:
    if(CentreX != 0):      
      Pturn = True
      color("yellow")
  spot(CentreX-1,CentreY-1, 35)
 # print (CentreX,CentreY,Array_X,Array_Y)
  
#if (gridarray[i,j-1] != 0):
#  update colour and array
#else
#  set up a goto
