import time
from turtle import Screen
import paddle
import ball
import scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("P O N G")
screen.tracer(0)

left_paddle = paddle.Paddle()
left_paddle.go_left()
right_paddle = paddle.Paddle()
right_paddle.go_right()
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 328 or ball.distance(left_paddle) < 50 and ball.xcor() < -328:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_point()


screen.exitonclick()
