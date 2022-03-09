from turtle import Turtle

FONT = ('Arial', 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.readFile()
        self.myScore = 0
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



    def resetScore(self):
        if self.myScore > self.highScore:
            self.updateHighScore(self.myScore)

        self.readFile()
        self.myScore = 0
        self.clear()
        self.goto(0, 310)
        self.write(f"Score: {self.myScore} High Score: {self.highScore}", True, align="center", font=FONT)


    def readFile(self):
        with open("score.txt", mode="r") as f:
            self.highScore = int(f.read())

    def updateHighScore(self, score):
        with open("score.txt", mode="w") as file:
            file.write(str(score))