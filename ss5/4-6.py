<<<<<<< HEAD
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

=======
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

>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
