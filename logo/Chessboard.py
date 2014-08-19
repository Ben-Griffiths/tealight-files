from tealight.logo import move, turn
def filled:
  filled = True
side = 80
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
def square_filled(side):
  for i in range(0,4):
    move(side)
    turn(90)
    
def Chessboard():
  if(filled == True):
    square_filled(side)
    filled = false
  else:
    square(side)
    filled = true
