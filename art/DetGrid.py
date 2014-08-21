from tealight.art import (color, line, spot, circle, box, image, text, background)

from github.griffithsben.art.connect4_defs import *

print grid_width
Array_X = 0
Array_Y = 0
CentreX = 0
CentreY = 0
Pturn = True
def handle_mousedown(x,y):
  global Array_X
  global Array_y
  global CentreX
  global CentreY
  global Pturn
  
      
  if(x >= 125 and x < 225):
    print  1
    Array_X = 0
    CentreX =175
  elif(x >= 225 and x < 325):
    print 2
    Array_X = 1
    CentreX = 275
  elif(x >= 325 and x < 425):
    print 3
    CentreX = 375
    Array_X = 2
  elif(x >= 425 and x < 525):
    print 4
    CentreX = 475
    Array_X = 3
  elif(x >= 525 and x < 625):
    print 5
    CentreX =575
    Array_X = 4
  elif(x >= 625 and x < 725):
    print 6
    CentreX = 675
    Array_X = 5
  elif(x >= 725 and x < 825):
    print 7
    CentreX = 775
    Array_X = 6    
  if(y >= 200 and y < 300):
    print 1
    CentreY = 250
    Array_Y = 0
  elif(y >= 300 and y < 400):
    print 2
    CentreY = 350
    Array_Y = 1
    
  elif(y >= 400 and y < 500):
    print 3
    CentreY = 450
    Array_Y = 2
  elif(y >= 500 and y < 600):
    print 4
    CentreY = 550
    Array_Y = 3
  elif(y >= 600 and y < 700):
    print 5
    CentreY = 650
    Array_Y = 4
  elif(y >= 700 and y < 800):
    print 6
    Array_Y = 5
  elif(y >= 800 and y < 900):
    print 7 
    CentreY = 750
    Array_Y = 6
  
  if (Pturn == True):
    Pturn = False
    if(CentreX != 0):         
      Pturn = False
      color("red")
      spot(CentreX-1,CentreY-1, 35)
    
  else:
    if(CentreX != 0):      
      Pturn = True
      color("yellow")
      spot(CentreX-1,CentreY-1, 35)
  