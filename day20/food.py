import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refesh()


    def refesh(self):
        corX = random.randint(-280, 280)
        corY = random.randint(-280, 280)
        self.goto(corX, corY)