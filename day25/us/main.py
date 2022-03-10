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

all_states = data['state'].to_list()
print(all_states)

def writeText(name, xCor, yCor):
    myT = turtle.Turtle()
    myT.penup()
    myT.hideturtle()
    myT.goto(xCor, yCor)
    myT.color("black")
    myT.write(name, align="center", font=("Arial", 12, "normal"))

guessed_states = []
score = 0

while True:
    answer = myScreen.textinput(f"Your Score {score}/{total}", "Name of a US State:").title()

    if answer == "Exit":
        break

    if answer in data['state'].to_list():
        guessed_states.append(answer)
        row = data[data['state'] == answer]
        xCor = row["x"].to_list()[0]
        yCor = row["y"].to_list()[0]
        print(f"{xCor}::{yCor}")
        score += 1
        writeText(answer, xCor, yCor)
    else:
        print("Wrong State")



not_guessed_states = [x for x in all_states if x not in guessed_states]

print(not_guessed_states)

with open("not_guessed_states.txt", mode="w") as fh:
    for x in not_guessed_states:
        fh.write(f"{x}\n")


#turtle.mainloop()
#myScreen.exitonclick()