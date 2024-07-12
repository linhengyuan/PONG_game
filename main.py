from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
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

game_is_on = True
while game_is_on:
    time.sleep(0.1) # delay screen update, let ball move slower, if without this code the ball will move like flash!
    screen.update() # refresh the screen manually
    ball.move()

    # bounce on the wall (top/down)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.change_dir_y()

    if ball.xcor() > 400 or ball.xcor() < -400:
        print("GAME OVER")
        game_is_on = False

screen.exitonclick()