#!/usr/bin/env python3

from snake import Snake
from turtle import Screen

# Create screen canvas
myS = Screen()
myS.listen()
myS.screensize(600, 600, "black")
myS.tracer(0)

# Init Snakes
snakeObj = Snake()
myS.update()


myS.onkey(snakeObj.moveUp, "Up")
myS.onkey(snakeObj.moveDown, "Down")
myS.onkey(snakeObj.moveRight, "Right")
myS.onkey(snakeObj.moveLeft, "Left")


while True:
    snakeObj.move()
    myS.update()


myS.exitonclick()