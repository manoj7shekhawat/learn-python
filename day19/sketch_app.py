#!/usr/bin/env python3
from turtle import Turtle, Screen

myT = Turtle()
myT.shape("turtle")
myT.shapesize(2)

def moveForward():
    myT.forward(50)

def moveBack():
    myT.backward(50)


def turnClockWise():
    myT.left(30)


def turnAntiClockWise():
    myT.right(30)


myS = Screen()
myS.listen()

def clear():
    myT.clear()
    myT.penup()
    myT.home()
    myT.pendown()

def makeCircle():
    myT.circle(50)

myS.onkey(fun=moveForward, key="d")
myS.onkey(fun=moveBack, key="a")
myS.onkey(fun=turnClockWise, key="s")
myS.onkey(fun=turnAntiClockWise, key="w")
myS.onkey(fun=clear, key="c")
myS.onkey(fun=makeCircle, key="r")

myS.exitonclick()