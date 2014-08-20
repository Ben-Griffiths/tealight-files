from tealight.art import (color, line, spot, circle, box, image, text, background)

x =00
y = 400
friction = 0.05
vx = 0
vy = 0
ax = 0 
ay = 0

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power
  

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
  if x == 0 or x == 900:
    vx = (-vx)
    ax = (-0.8 * ax) 
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = (vx*0.98) + ax 
  vy = (vy*0.98) + ay + 0.1
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
def handle_keydown(key):
   if x == 0 or x == 900:
    vx = (-vx)
    ax = (-0.8 * ax) 
  
  
    