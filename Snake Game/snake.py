from turtle import Turtle
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in range(20,-40,-20):
            self.extend((i,0))

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].setpos(self.segments[i-1].pos())
        self.head.fd(MOVE_DISTANCE)

    def extend(self,pos):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def add(self):
        self.extend(self.segments[-1].pos())

    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() !=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)