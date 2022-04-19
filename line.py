from turtle import Turtle
WALL=280

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_line()


    def draw_line(self):
        self.penup()
        self.goto(-WALL, WALL)
        self.hideturtle()
        self.pendown()
        self.color('red')
        self.setpos(-WALL, -WALL)
        self.setpos(WALL, -WALL)
        self.setpos(WALL, WALL)
        self.setpos(-WALL, WALL)
