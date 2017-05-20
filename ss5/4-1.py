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
    
