from turtle import Turtle
import time

MOVE_DISTANCE = 20

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:

    def __init__(self):
        self.snakes = []
        self.createSnakes()

    def createSnakes(self):
        xCor = 0
        for x in range(0, 3):
            myT = Turtle()
            myT.penup()
            myT.shape("square")
            myT.color("white")
            myT.goto(xCor, 0)
            xCor += -20
            self.snakes.append(myT)

    def move(self):
        time.sleep(0.1)
        for x in range(len(self.snakes) - 1, 0, -1):
            newX = self.snakes[x - 1].xcor()
            newY = self.snakes[x - 1].ycor()
            self.snakes[x].goto(newX, newY)
        self.snakes[0].forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.snakes[0].heading() != SOUTH:
            self.snakes[0].setheading(NORTH)

    def moveDown(self):
        if self.snakes[0].heading() != NORTH:
            self.snakes[0].setheading(SOUTH)

    def moveLeft(self):
        if self.snakes[0].heading() != EAST:
            self.snakes[0].setheading(WEST)

    def moveRight(self):
        if self.snakes[0].heading() != WEST:
            self.snakes[0].setheading(EAST)
