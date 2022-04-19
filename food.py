from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('green')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        #self.speed('fastest')
        self.more()

    def more(self):
        x_cor = random.randint(-260,260)
        y_cor = random.randint(-260,260)
        self.goto(x_cor,y_cor)




