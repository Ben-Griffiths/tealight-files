from tealight.logo import move, turn

def Chessboard():
  for i in range (0,4):
     move(80)
     turn(90)
     move(10)
     turn(90)
     move(-8)
     turn(90)
      
Chessboard()    
