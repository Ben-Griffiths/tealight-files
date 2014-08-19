from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while true:
  move()
  if(left_side() == "fruit"):
    turn(-1)
    move()
  else if(right_side() == "fruit"):
    turn(1)
    move()
  else if (look == "fruit"):
    while (look == "fruit"):
      move()
  if(touch == "wall"):
    if(left_side != "wall"):
      turn(-1)
    else if(rightside != "wall"):
      turn(1)
  

    