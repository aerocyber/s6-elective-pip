#!/usr/bin/env python3

import turtle 
import math

n=int(input("Enter the number of stars:\t"))

t=turtle.Turtle()
t.penup()
t.goto(100, 0)
t.penup()

def star():
    t.pencolor("gold")
    t.fillcolor("gold")
    t.begin_fill()
    t.right(36)  
    for i in range(5):  
        t.forward(50)
        t.right(144)  
        t.forward(50)
        t.left(72)  
    t.end_fill()

for i in range(n):

    angle = (360 / n) * i
    x = 300 * math.cos(math.radians(angle))
    y = 300 * math.sin(math.radians(angle))
    t.goto(x, y)
    t.down()
    star()
    t.up()

t.goto(0,0)
t.hideturtle()
        

