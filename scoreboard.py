from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    #Draw the score on the screen
    def increase_score(self):
        #deleting the previous score using undo()
        self.clear()
        self.score +=1
        self.update_scoreboard()

