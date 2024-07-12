from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score, Net
import time

# set screen background size, color
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0) # close the animation, so we need to refresh the screen manually

# create paddle
paddle_right = Paddle(x_axis=350, y_axis=0)
paddle_left = Paddle(x_axis=-350, y_axis=0)

# create paddle and set control key
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

# create ball object
ball = Ball()

# Create scoreboard object
score = Score()
net = Net()

game_is_on = True
while game_is_on:
    time.sleep(0.1) # delay screen update, let ball move slower, if without this code the ball will move like flash!
    screen.update() # refresh the screen manually
    ball.move()

    # bounce on the wall (top/down)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_dir_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330 or ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.change_dir_x()

    # Detect right paddle miss
    if ball.xcor() > 400 :
        ball.reset_position()
        score.on_point_to_left()

    # Detect left paddle miss
    if ball.xcor() < -400:
        ball.reset_position()
        score.on_point_to_right()

    if score.score_left > 1 or score.score_right > 1:
        game_is_on = False
        score.game_over()

screen.exitonclick()