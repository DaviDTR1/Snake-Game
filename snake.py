from random import randint
from turtle import Turtle,Screen, right

from requests import delete
MoveDistance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.game_on = True
        self.is_move = False
        self.create_snake()

    def point_up(self):
        if self.snake[0].heading() != DOWN and not self.is_move:
            self.snake[0].setheading(UP)
            self.is_move = True
    def point_down(self):
        if self.snake[0].heading() != UP and not self.is_move:
            self.snake[0].setheading(DOWN)
            self.is_move = True
    def point_right(self):
        if self.snake[0].heading() != LEFT and not self.is_move:
            self.snake[0].setheading(RIGHT)
            self.is_move = True
    def point_left(self):
        if self.snake[0].heading() != RIGHT and not self.is_move:
            self.snake[0].setheading(LEFT)
            self.is_move = True

    def move(self):
        xpos = 0
        ypos = 0
        
        for i in range(len(self.snake)-1,-1,-1):
            if i == 0:
                self.snake[i].forward(MoveDistance)
                xpos = self.snake[i].xcor()
                ypos = self.snake[i].ycor()
                for j in range(1,len(self.snake)):
                    if self.snake[j].distance(self.snake[0]) < 15:
                        self.game_on = False
                        break
                if xpos > 290 or xpos < -290 or ypos >= 280 or ypos <= -290:
                    self.game_on = False
            else:
                xpos = self.snake[i-1].xcor()
                ypos = self.snake[i-1].ycor()
                self.snake[i].goto(xpos,ypos)
        self.is_move = False
    
    def is_game_on(self):
        return self.game_on
    
    def get_score(self):
        return self.score    

    def eat(self, food):
        lastx = self.snake[-1].xcor()
        lasty = self.snake[-1].ycor()
        
        if self.snake[0].distance(food) < 15:
            n_snake = Turtle()
            n_snake.shape("square")
            n_snake.shapesize(1,1,0)
            n_snake.speed("slowest")
            n_snake.color("white")
            n_snake.penup()
            n_snake.goto(lastx,lasty)
            self.snake.append(n_snake)
            return True
    
    def create_snake(self):
        for i in range(0,3):
            n_snake = Turtle()
            n_snake.shape("square")
            n_snake.shapesize(1,1,0)
            n_snake.speed("slowest")
            n_snake.color("white")
            n_snake.penup()
            if i > 0:
                xpos = self.snake[i-1].xcor()
                n_snake.goto(xpos-20,0)
            self.snake.append(n_snake)
    
    def reset(self):
        for seg in self.snake:
            seg.hideturtle()
            del seg
        self.snake.clear()
        self.create_snake()
        self.game_on = True
            