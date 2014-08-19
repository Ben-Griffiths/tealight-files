from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(1,51):
  move(i)
  turn(27)
  color(colors[i%3])