from ball import Ball
from paddle import Paddle
from screensetup import ScreenSetUp
from scoreboard import Scoreboard
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen = ScreenSetUp(r_paddle, l_paddle)
ball = Ball()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(0.01)
    screen.screen.update()
    ball.move_ball()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) <= 50 and ball.xcor() > 330) or (ball.distance(l_paddle) <= 50 and ball.xcor() < -330):
        ball.bounce_x()
    if ball.xcor() > 350:
        ball.reset_ball()
        scoreboard.l_point()
    if ball.xcor() < -350:
        ball.reset_ball()
        scoreboard.r_point()
screen.screen.exitonclick()
