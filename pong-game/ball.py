from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.color('pink')
        self.xFactor = 2
        self.yFactor = -2
        self.ball_speed = 1

    def move_ball(self):
        new_x = self.xcor() + self.xFactor * self.ball_speed
        new_y = self.ycor() + self.yFactor * self.ball_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.yFactor *= -1

    def bounce_x(self):
        self.ball_speed += .1
        self.xFactor *= -1

    def reset_ball(self):
        self.bounce_x()
        self.ball_speed = 1
        self.goto(0, 0)
