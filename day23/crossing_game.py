from turtle import Screen
from car import Car
from player import Player
from score import Score

import random
import time


myScreen = Screen()
myScreen.title("CrossRoad Game")
myScreen.setup( width=800, height=600)
myScreen.bgcolor("white")
# For random color of car
myScreen.colormode(255)
# Update the screen only with update function
myScreen.tracer(0)
# Listen for key input
myScreen.listen()

# Create car
cars = []
cars.append(Car())

# Init Player
player = Player()
# Init Score
score = Score()

# For key input
myScreen.onkey(player.move, "Up")

gameIsOn = True
sleep = 0.1

while gameIsOn:
    # Sleep for some time
    time.sleep(sleep)

    # Update the screen
    myScreen.update()

    # randomly generate cars
    if random.randint(0, 5) == 5:
        cars.append(Car())

    # move cars
    for c in cars:
        c.move()
        # Check collision
        if player.distance(c) < 40:
            score.gameOver()
            gameIsOn = False
            break


    # Increment score, reset player position and increase speed
    if player.ycor() > 265:
        score.levelUp()
        player.reset()
        sleep *= 0.9


# Click on exist
myScreen.exitonclick()