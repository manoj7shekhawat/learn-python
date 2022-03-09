from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.createCar()


    def createCar(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=2)
        self.color(self.getColor())
        self.goto(400, random.randint(-220, 220))


    def getColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)


    def move(self):
        self.backward(20)