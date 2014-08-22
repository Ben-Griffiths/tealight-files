from tealight.art import (color, line, spot, circle, font, box, image, text, background)
from github.andyandywells.art.matrixFunctions import *
from github.griffithsben.art.connect4_defs import *

matrix = initialiseMatrix()


Pturn = 1

def handle_mousedown(x,y):
  global Pturn
  Array_X = (x - offset_x) // cell_size #sets xcoord for array from click
  Array_Y = (y - offset_y) // cell_size #sets ycoord for array from click
  if(Array_X >=7 or Array_X <0 or Array_Y <0  or Array_Y >= 7):
    return 0 #breaks function if outside of grid without switching
    
  CentreX = (Array_X+1)*100+75 #finds centre point for dot as below
  CentreY = (2+Array_Y)*100 +50 
  
  
  # if (matrix[Array_Y-1][Array_X] != 0):
  if (Array_Y == 6 or matrix[Array_Y+1][Array_X] != 0 ):
      if matrix[Array_Y][Array_X] == 0: #!= 1 or matrix[Array_Y][Array_X] != -1:
        if Pturn == 1:
          print(Array_X)
          print(Array_Y)
          color("red")
          Pturn = -1
        else:
           print(Array_X)
           print(Array_Y)
           color("yellow")
           Pturn = 1   
        
        spot(CentreX-1, CentreY-1, 35)
        matrix[Array_Y][Array_X] = -Pturn       
        
        if checkwin(matrix) == True:        
          print("Red wins")
        #  color("red")
          image(125,200, "https://photos-2.dropbox.com/t/0/AAADMd5_ZYX1JR1o2m2Wcn-smmLnF1NQCdP_dF0rf8PdUA/12/85596892/png/1024x768/3/1408705200/0/2/RED_WINS.png/2RKVLGw4E8Oh-w3vRAduhboRA1CZEgjUl5W70FAWTdc")    
          
        elif checkwin(matrix) == False:
          print("P2 wins")   
          image(125,200,"https://photos-3.dropbox.com/t/0/AAAQatRVEnQ5-zZZJKOkmSlPE78GJ3la0QewGPWgaNkBZA/12/85596892/png/1024x768/3/1408705200/0/2/YELLOW_WINS.png/eIEUmrzdj3JywkWfYV6ScacXMdkSRb5PkVLiumDJiDo")
        return 0
  

