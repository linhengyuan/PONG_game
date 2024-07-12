from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_distance_y = 15
        self.move_distance_x = 15

    def move(self):
        new_x = self.xcor() + self.move_distance_x
        new_y = self.ycor() + self.move_distance_y
        self.goto(new_x, new_y)

    def change_dir_x(self):
        self.move_distance_x = self.move_distance_x * (-1)

    def change_dir_y(self):
        self.move_distance_y = self.move_distance_y * (-1)