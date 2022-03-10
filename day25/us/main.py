import turtle
from turtle import Screen

import pandas as pd

imageName = "blank_states_img.gif"

myScreen = Screen()
myScreen.title("US Game")
myScreen.addshape(imageName)

turtle.shape(imageName)


data = pd.read_csv("50_states.csv")

total = data['state'].count()

def writeText(name, xCor, yCor):
    myT = turtle.Turtle()
    myT.penup()
    myT.hideturtle()
    myT.goto(xCor, yCor)
    myT.color("black")
    myT.write(name, align="center", font=("Arial", 12, "normal"))

score = 0
while True:
    answer = myScreen.textinput(f"Your Score {score}/{total}", "Name of a US State:").title()
    if answer in data['state'].to_list():
        row = data[data['state'] == answer]
        xCor = row["x"].to_list()[0]
        yCor = row["y"].to_list()[0]
        print(f"{xCor}::{yCor}")
        score += 1
        writeText(answer, xCor, yCor)
    else:
        print("Wrong State")




turtle.mainloop()
#myScreen.exitonclick()