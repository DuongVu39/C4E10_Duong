from turtle import *

bgcolor("lightgreen") #Set the windown background color
color('pink', 'pink')

speed = 1
def draw_square(m):
    for i in range(4):
        fd(m)
        left(90)

def ex2(n):
    m = 20
    for i in range(n):
        draw_square(m)
        penup()
        right(135)
        fd(13)
        left(135)
        pendown()
        m += 20
        
ex2(5)
    
