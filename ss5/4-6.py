from turtle import *

bgcolor('lightgreen')
color('blue')
t= Turtle()

def draw_poly (t, n, sz):
    t = Turtle()
    for i in range (n):
        t.fd(sz)
        t.left(360/n)

def draw_equitriangle (t,sz):
    draw_poly(t,3,sz)

draw_equitriangle (t, 50)

