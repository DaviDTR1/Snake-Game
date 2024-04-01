from random import randint
import time
from tkinter import CENTER
from tracemalloc import start
from turtle import Turtle,Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
part = 2

while True:
    screen.update()
    screen.onkey(key="Up",fun=snake.point_up)
    screen.onkey(key="Down",fun=snake.point_down)
    screen.onkey(key="Right",fun=snake.point_right)
    screen.onkey(key="Left",fun=snake.point_left)
    snake.move()
    if snake.eat(food):
        food.change_position()
    
    scoreboard.print_score(len(snake.snake)-3) 
    
    time.sleep(0.1)
    if snake.is_game_on() == False:
        scoreboard.reset(len(snake.snake)-3)
        snake.reset()
     

screen.exitonclick()