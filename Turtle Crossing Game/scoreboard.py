from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0,220)
        self.level=1
        self.update_scorecard()
    
    def update_scorecard(self):
        self.write(f"Level: {self.level}",align="center",font=("Courier",20,"normal"))
    
    def point(self):
        self.level+=1
        self.clear()
        self.update_scorecard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",20,"normal"))