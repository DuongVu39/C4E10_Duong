<<<<<<< HEAD
from turtle import *

def draw_star(x,y,n):
    setposition(x, y)
    for i in range(5):
        fd(n)
        left(144)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
=======
from turtle import *

def draw_star(x,y,n):
    setposition(x, y)
    for i in range(5):
        fd(n)
        left(144)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
