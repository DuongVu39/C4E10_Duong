from turtle import *

def draw_a_star(n):
    for i in range(5):
        fd(n)
        left(144)
def ex10(m,n):
    for i in range(m):
        draw_a_star(n)
        penup()
        fd(350)
        right(144)
        pendown()

ex10(5,100)
