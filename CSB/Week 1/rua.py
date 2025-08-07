import math
from turtle import *
  
# Triangle
for i in range(3):
    forward(100)
    left(120)

#penup
left(180)
penup()
forward(100)
pendown()

#Picture frame
for i in range(4):
    width(4)
    forward(100)
    right(90)
penup()
right(45)
forward(math.sqrt(50))
pendown()
left(45)
for i in range(4):
    width(1)
    forward(90)
    right(90)

#penup
penup()
left(90)
forward(110)
left(90)
pendown()

#weird
for i in range(4):
    width(2)
    forward(100)
    right(90)

penup()
right(45)
forward(math.sqrt(20000)/2)
left(45)
forward(math.sqrt(20000)/2)
left(90 + 45)
pendown()

for i in range(4):
    width(1)
    forward(100)
    left(90)

mainloop()