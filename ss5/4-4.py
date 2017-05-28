<<<<<<< HEAD
from turtle import *

bgcolor('lightgreen')
color('blue')
speed (-1)
def draw_square():
    for i in range (4):
        fd(100)
        left(90)

def draw_pattern(n):
    for i in range (n):
        draw_square()
        left(18)

draw_pattern(20)
=======
from turtle import *

bgcolor('lightgreen')
color('blue')
speed (-1)
def draw_square():
    for i in range (4):
        fd(100)
        left(90)

def draw_pattern(n):
    for i in range (n):
        draw_square()
        left(18)

draw_pattern(20)
>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
