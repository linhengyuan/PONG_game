from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        # self.penup()
        self.add_paddle(x_axis=350, y_axis=0)
        self.add_paddle(x_axis=-350, y_axis=0)

    def add_paddle(self, x_axis, y_axis):
        new_paddle = Turtle("square")
        new_paddle.hideturtle()
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.goto(x=x_axis, y=y_axis)
        new_paddle.turtlesize(stretch_wid=5, stretch_len=1)
        new_paddle.showturtle()
