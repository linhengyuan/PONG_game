from turtle import Turtle

MOVE_DISTANCE = 100
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.speed(10)
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=self.x_axis, y=self.y_axis)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)