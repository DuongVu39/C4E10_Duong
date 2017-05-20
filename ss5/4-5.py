from turtle import *
bgcolor('lightgreen')
color('blue')
speed (-1)

def draw_pattern(n):
    m = 5
    for i in range (n):
        for j in range (4):
            right(90)
            fd(m)
            m += 4
        left (5)
draw_pattern(100)




