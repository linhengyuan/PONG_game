import time
from turtle import Turtle
from random import randint, choice

SERVE_DIRECTION = [-1, 1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_distance_y = randint(8,15) * choice(SERVE_DIRECTION)
        self.move_distance_x = randint(8,15) * choice(SERVE_DIRECTION)

    def move(self):
        new_x = self.xcor() + self.move_distance_x
        new_y = self.ycor() + self.move_distance_y
        self.goto(new_x, new_y)

    def change_dir_x(self):
        self.move_distance_x *= -1

    def change_dir_y(self):
        self.move_distance_y *= -1

    # reset the position of ball, and change direction
    def reset_position(self):
        self.goto(0,0)
        time.sleep(1)
        self.change_dir_x()