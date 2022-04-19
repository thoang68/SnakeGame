import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from line import Line
WALL = 280

screen = Screen()
screen.setup(width=600, height=600)

#Issue with small window in Replit: User may need to minimize the Console/Shell window
ready_to_play=screen.textinput("WARNING for Replit users", "Please minimize the Console/Shell window below. Are you ready? (Y/N)").lower()

screen.bgcolor('black')
screen.title('My Snake Game')
#turn off the update on the screen to avoid seeing spaces between segments (turtles)
screen.tracer(0)

line = Line()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


if ready_to_play == 'y':
    is_game_on=True
else:
    is_game_on=False

while is_game_on:
    # update and show the final state of all the segment
    screen.update()
    # hang 0.2 sec after each for loop. This will decide the speed for snake
    time.sleep(0.2)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.grow()
        food.more()

    #Detect collison with walls
    if -WALL <= snake.head.xcor() <= WALL and -WALL <= snake.head.ycor() <= WALL:
        pass
    else:
        is_game_on=False
        scoreboard.game_over()

    #Detect collision with tail: happens when head hits any of the segments
    # for seg in snake.all_segments:
    #     if seg ==  snake.head:
    #         pass
    #     elif snake.head.distance(seg) <10:
    #         is_game_on=False
    #         scoreboard.game_over()

    for seg in snake.all_segments[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            scoreboard.game_over()







screen.exitonclick()