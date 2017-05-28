<<<<<<< HEAD
from turtle import *

bgcolor("lightgreen") #Set the windown background color
color('pink', 'pink')

def draw_square():
    for i in range(4):
        fd(20)
        left(90)

def ex1(n):

    for i in range(n):
        draw_square()
        penup()
        fd(40)
        pendown()
begin_fill()
ex1(5)
end_fill()
    
=======
from turtle import *

bgcolor("lightgreen") #Set the windown background color
color('pink', 'pink')

def draw_square():
    for i in range(4):
        fd(20)
        left(90)

def ex1(n):

    for i in range(n):
        draw_square()
        penup()
        fd(40)
        pendown()
begin_fill()
ex1(5)
end_fill()
    
>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
