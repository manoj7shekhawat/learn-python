from turtle import Turtle


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.displayScore()


    def displayScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 20, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 20, "normal"))


    def rScores(self):
        self.r_score += 1
        self.displayScore()


    def lScores(self):
        self.l_score += 1
        self.displayScore()