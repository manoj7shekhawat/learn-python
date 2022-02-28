#!/usr/bin/env python3
import random
import turtle
from turtle import Turtle, Screen

myT = Turtle()
myT.shape("turtle")
myT.color("green")

# Make square
# for x in range(1, 5):
#     myT.forward(100)
#     myT.right(90)

# Make dashed line
# myT.shapesize(2)
# print(myT.position())
# myT.hideturtle()
# myT.penup()
# myT.setpos(-450,0.00)
# myT.showturtle()
# for x in range(0, 50):
#     if x % 2 == 0:
#         myT.pendown()
#         myT.forward(10)
#     else:
#         myT.penup()
#         myT.forward(10)


# Make different shapes 3-10
# myT.shapesize(2)
# colors = ["green", "red", "blue", "orange", "gold", "black", "purple", "pink"]
# angle = 360
# for x in range(3, 11):
#     myT.color(colors[x-3])
#     for y in range(0, x):
#         myT.forward(125)
#         myT.left(int(angle/x))


# Make random walk
# myT.speed("normal")
# myT.pensize(15)
# #colors = ["green", "red", "blue", "orange", "gold", "black", "purple", "pink", "yellow", "brown", "#000099"]
# turtle.colormode(255)
#
# def generateColor():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     myTup = (r, g, b)
#     return myTup
#
#
# angles = [90, 180, 270, 360]
# for x in range(0, 100):
#     #myT.color(random.choice(colors))
#     myT.color(generateColor())
#     myT.forward(75)
#     myT.left(random.choice(angles))

# Spirograph
turtle.colormode(255)

def generateColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    myTup = (r, g, b)
    return myTup


for x in range(0, 359, 5):
    myT.color(generateColor())
    myT.right(5)
    myT.circle(175)

myS = Screen()
#myS.clear()
myS.exitonclick()