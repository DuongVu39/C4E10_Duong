from turtle import *

bgcolor('lightgreen')
color('pink')

def draw_poly (t, n, sz):
    t = Turtle()
    for i in range (n):
        t.fd(sz)
        t.left(360/n)
    

draw_poly(tess, 8, 50)
