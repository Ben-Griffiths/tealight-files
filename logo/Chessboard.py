from tealight.logo import move, turn
side = 80
def square(side):
  for i in range(0,3):
    move(side)
    turn(90)
    if(i == 4):
      move(-80)
def square_filled(side):
  for i in range(0,3):
    move(side)
    turn(90)
    if(i == 4):
      move(-80)
    
def Chessboard(filled):
  if(filled == True):
    square_filled(side)
    filled = False
  else:
    square(side)
    filled = True
for i in range(0,8):
  Chessboard(True)