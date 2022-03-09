from turtle import Turtle

FONT = ('Arial', 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.myScore = 0
        self.highScore = 0
        self.penup()
        self.goto(0, 310)
        self.color("white")
        self.write(f"Score: {self.myScore} High Score: {self.highScore}", True, align="center", font=FONT)
        self.hideturtle()



    def increaseScore(self):
        self.myScore += 1
        self.clear()
        self.goto(0, 310)
        self.write(f"Score: {self.myScore} High Score: {self.highScore}", True, align="center", font=FONT)


    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", True, align="center", font=FONT)



    def resetScore(self):
        if self.myScore > self.highScore:
            self.highScore = self.myScore
        self.myScore = 0
        self.clear()
        self.goto(0, 310)
        self.write(f"Score: {self.myScore} High Score: {self.highScore}", True, align="center", font=FONT)