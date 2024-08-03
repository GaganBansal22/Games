from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.pu()
        self.goto(pos)

    def go_up(self):
        if(self.ycor()<200):
            self.goto(self.xcor(),self.ycor()+20)

    def go_down(self):
        if(self.ycor()>-200):
            self.goto(self.xcor(),self.ycor()-20)