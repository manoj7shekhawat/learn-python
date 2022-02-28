#!/usr/bin/env python3

import random
import turtle

import colorgram
from turtle import Turtle, Screen

# Extract 30 colors from an image.
colors = colorgram.extract('spot_painting.jpeg', 30)

colorsList = []

for x in range(0, 30):
    first_color = colors[x]
    rgb = first_color.rgb # e.g. (255, 151, 210)
    colorsList.append((rgb.r, rgb.g, rgb.b))


#print(colorsList)


turtle.colormode(255)

myT = Turtle()
myT.shape("turtle")
myT.shapesize(2)
myT.speed("fast")
# Y position
count = -200.0

for x in range(0, 10):

    # Hide turtle
    myT.hideturtle()
    # Pen up turtle
    myT.penup()
    # X, Y position
    myT.setpos(-450, count)
    # Show turtle
    myT.showturtle()

    for y in range (0, 20):
        if y % 2 == 0:
            myT.penup()
            myT.forward(50)
        else:
            myT.pendown()
            myT.dot(25, random.choice(colorsList))

    count += 50.0

myS = Screen()
myS.exitonclick()