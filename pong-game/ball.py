from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.color('pink')
        self.xFactor = .2
        self.yFactor = -.2

    def move_ball(self):
        newX = self.xcor() + self.xFactor
        newY = self.ycor() + self.yFactor
        self.goto(newX, newY)

    def bounce_y(self):
        self.yFactor *= -1

    def bounce_x(self):
        self.xFactor *= -1

    def reset_ball(self):
        self.goto(0,0)
