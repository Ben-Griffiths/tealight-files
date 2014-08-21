from tealight.art import (color, line, spot, circle, box, image, text, background)
Array_X = 0
Array_Y = 0
def handle_mousedown(x,y):
  global Array_X
  global Array_y
  spot(x,y,10)
  Array_X = x
  Array_Y = y
    
  if(x >= 125 and x < 225):
    print  1
  elif(x >= 225 and x < 325):
    print 2
  elif(x >= 325 and x < 425):
    print 3
  elif(x >= 425 and x < 525):
     print 4
  elif(x >= 525 and x < 625):
    print 5
  elif(x >= 625 and x < 725):
    print 6
  elif(x >= 725 and x < 825):
    print 7
    
  if(y >= 200 and y < 300):
    print 1
  elif(y >= 300 and y < 400):
    print 2
  elif(y >= 400 and y < 500):
    print 3
  elif(y >= 500 and y < 600):
     print 4
  elif(y >= 600 and y < 700):
    print 5
  elif(y >= 700 and y < 800):
    print 6
  elif(y >= 800 and y < 900):
    print 7  
  
  


  
  
  