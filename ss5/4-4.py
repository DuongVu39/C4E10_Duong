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
