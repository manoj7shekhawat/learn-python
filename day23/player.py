from turtle import Turtle

class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -265)
        self.shape("turtle")
        self.shapesize(2)
        self.color("green")
        self.setheading(90)


    def move(self):
        self.forward(20)


    def reset(self):
        self.goto(0, -265)