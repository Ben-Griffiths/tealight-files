from tealight.logo import move, turn
side = 80
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
def square_filled(side):
  for i in range(0,4):
    move(side)
    turn(-90)
    
def Chessboard(filled):
  if(filled == True):
    square_filled(side)
    filled = False
  else:
    square(side)
    filled = True 
Chessboard(True)