from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(-100,170)
        self.write(self.l_score,align="center",font=("Courier",60,"normal"))
        self.goto(100,170)
        self.write(self.r_score,align="center",font=("Courier",60,"normal"))

    def point(self,n):
        if(n==0):
            self.l_score+=1
        else:
            self.r_score+=1
        self.clear()
        self.update_scoreboard()