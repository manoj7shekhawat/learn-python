#!/usr/bin/env python3
import random
from turtle import Turtle, Screen

# def getColor():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     myTup = (r, g, b)
#     return myTup


colors = ["red", "green", "blue", "black", "purple", "pink", "yellow"]

myS = Screen()
mybet = myS.textinput(f"Your Bet", f"Which turtle you bet on? {colors}: ")

turtles = []

yCordinat = -250.00

for x in range(0, 7):
    myT = Turtle()
    myT.shape("turtle")
    myT.shapesize(2)
    myT.color(colors[x])
    myT.penup()
    turtles.append(myT)

    myT.setpos(-450, yCordinat)
    yCordinat += 100

# race begins
for x in range(0, 400):
    randT = random.randint(0, 6)
    turtles[randT].speed(random.randint(0, 10))
    turtles[randT].forward(10)


maxPos = 0
winner = 0
for x in range(0, 7):
    myP = round(turtles[x].xcor(), 2)
    if maxPos < myP:
        maxPos = myP
        winner = x

if colors[winner] == mybet:
    print("Yeah you won!!!")
else:
    print(f"Sorry you lost. The winner is {colors[winner]} turtle")

myS.exitonclick()