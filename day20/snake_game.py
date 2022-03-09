#!/usr/bin/env python3

from snake import Snake
from turtle import Screen
from food import Food
from score import Score

# Create screen canvas
myS = Screen()
myS.listen()
myS.screensize(600, 600, "black")
myS.tracer(0)

# Init Snakes
snakeObj = Snake()
food = Food()
score = Score()

myS.update()


myS.onkey(snakeObj.moveUp, "Up")
myS.onkey(snakeObj.moveDown, "Down")
myS.onkey(snakeObj.moveRight, "Right")
myS.onkey(snakeObj.moveLeft, "Left")

gameOn = True

while True:
    snakeObj.move()
    myS.update()

    # If distance is less than 15 then there is collision
    if snakeObj.snakes[0].distance(food) < 15:
        food.refesh()
        score.increaseScore()
        snakeObj.addSnake()


    # Out of boundary
    if snakeObj.snakes[0].xcor() > 450 or snakeObj.snakes[0].xcor() < -450 or snakeObj.snakes[0].ycor() > 385 or snakeObj.snakes[0].ycor() < -385:
        snakeObj.reset()
        score.resetScore()


    # If collided with tail
    for sn in snakeObj.snakes[1:]:
        if snakeObj.snakes[0].distance(sn) < 5:
            snakeObj.reset()
            score.resetScore()


myS.exitonclick()