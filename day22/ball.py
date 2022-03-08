from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.xcord = 12
        self.ycord = 10


    def move(self):
        self.goto(self.xcor() + self.xcord, self.ycor() + self.ycord)


    def bounce_y(self):
        self.ycord *= -1


    def bounce_x(self):
        self.xcord *= -1


    def reset(self):
        self.xcord *= -1
        self.ycord *= -1
        self.goto(0, 0)