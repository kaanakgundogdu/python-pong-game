from ball import Ball
from paddle import Paddle
from screensetup import ScreenSetUp
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen = ScreenSetUp(r_paddle, l_paddle)
ball = Ball()

is_game_on = True
while is_game_on:
    screen.screen.update()
    ball.move_ball()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) <= 50 and ball.xcor()>330) or (ball.distance(l_paddle) <= 50 and ball.xcor()<-330):
        ball.bounce_x()
    elif (ball.xcor()>330) or ball.xcor()<-330:
        ball.reset_ball()

screen.screen.exitonclick()
