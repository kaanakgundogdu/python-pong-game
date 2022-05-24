from turtle import Turtle, Screen
from paddle import Paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen = Screen()

screen.setup(800, 600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
