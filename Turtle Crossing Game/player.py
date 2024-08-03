from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.reset_player()

    def finish(self):
        self.reset_player()

    def reset_player(self):
        self.goto(0,-230)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+10)