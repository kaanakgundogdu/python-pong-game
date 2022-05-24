from turtle import Screen


class ScreenSetUp:
    def __init__(self, r_paddle, l_paddle):
        self.screen = Screen()

        self.screen.setup(800, 600)
        self.screen.bgcolor('black')
        self.screen.title('PONG')
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(r_paddle.go_up, 'Up')
        self.screen.onkeypress(r_paddle.go_down, 'Down')
        self.screen.onkeypress(l_paddle.go_up, 'w')
        self.screen.onkeypress(l_paddle.go_down, 's')
