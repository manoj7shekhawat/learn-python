from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.myScore = 1
        self.penup()
        self.hideturtle()
        self.goto(-300, 250)
        self.color("black")
        self.write(f"Level: {self.myScore}", align='center', font=('Arial', 16, 'normal'))


    def levelUp(self):
        self.myScore += 1
        self.clear()
        self.write(f"Level: {self.myScore}", align='center', font=('Arial', 16, 'normal'))


    def gameOver(self):
        myT = Turtle()
        myT.penup()
        myT.hideturtle()
        myT.color("black")
        myT.write(f"GAME OVER", align='center', font=('Arial', 16, 'normal'))