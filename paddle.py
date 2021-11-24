import turtle


class Paddle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(5, 1)
        self.score = 0

    def go_right(self):
        self.setpos(350, 0)

    def go_left(self):
        self.setpos(-350, 0)

    def up(self):
        current_y = self.ycor()
        if current_y < 260:
            self.sety(current_y + 20)

    def down(self):
        current_y = self.ycor()
        if current_y > -260:
            self.sety(current_y - 20)

    def update_score(self):
        self.score += 1





