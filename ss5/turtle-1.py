from turtle import *
speed (-1)
def draw_square(l, c):
    color(c)
    for i in range(4):
        fd(l)
        left(90)

##draw_square(100,"red")

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
