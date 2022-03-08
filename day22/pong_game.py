from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


myScreen = Screen()
myScreen.listen()
myScreen.bgcolor("black")
myScreen.setup(800, 600)
myScreen.title("Pong Game")
myScreen.tracer(0)

# Create Paddle Obj
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

score = ScoreBoard()
score.displayScore()

# Event handlers
myScreen.onkey(r_paddle.moveUp, key="Up")
myScreen.onkey(r_paddle.moveDown, key="Down")

myScreen.onkey(l_paddle.moveUp, key="w")
myScreen.onkey(l_paddle.moveDown, key="s")

gameIsOn = True

speed = 0.1
while gameIsOn:
    time.sleep(speed)
    myScreen.update()

    # when ball crosses the horizontal line
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # when the ball crosses the vertical boundary and collide wih the paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        speed *= 0.9

    if ball.xcor() > 340:
        ball.reset()
        speed = 0.1
        score.lScores()

    if ball.xcor() < -340:
        ball.reset()
        speed = 0.1
        score.rScores()

    ball.move()


myScreen.exitonclick()