from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while True:
  move()
 # if(left_side() == "fruit"):
 #   turn(-1)
  elif(right_side() == "fruit"):
    turn(1)
  elif (look() == "fruit"):
    while (look() == "fruit"):
      move()
  if(left_side() == None):
    turn(-1)
    move() 
   
  if(touch() == "wall"):
    if(left_side() != "wall"):
      turn(-1)
      move()
    elif(right_side() != "wall"):
      turn(1) 
      move()
    else:
      turn(2)
      move()
  