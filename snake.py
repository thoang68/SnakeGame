from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        # define self.head since self.all_segments[0] will be used a lot
        self.head = self.all_segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def grow(self):
        #the new segment will go to the last segment
        self.add_segment(self.all_segments[-1].position())

    def move(self):
            # move the last segment to the position of the next one, and so on.
            for seg_num in range(len(self.all_segments) - 1, 0, -1):
                new_x = self.all_segments[seg_num - 1].xcor()
                new_y = self.all_segments[seg_num - 1].ycor()
                self.all_segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Go North - Up. Snake cannot go up if the heading is down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Go South - Down. Snake cannot go down if the heading is up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        #Go West - Left. Snake cannot go left if the heading is right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        #Go East - Right. Snake cannot go right if the heading is left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

