import turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.speed(4)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_reset(self):
        self.move_speed = 0.1
        self.home()
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
