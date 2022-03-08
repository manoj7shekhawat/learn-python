from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xCor, yCor):
        super().__init__()
        self.createPaddle(xCor, yCor)


    def createPaddle(self, xCor, yCor):
        self.penup()
        self.goto(xCor, yCor)
        self.shapesize(stretch_wid=None, stretch_len=5)
        self.left(90)
        self.color("white")
        self.shape("square")


    def moveUp(self):
        self.forward(20)


    def moveDown(self):
        self.backward(20)