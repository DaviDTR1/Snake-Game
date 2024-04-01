from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(-10,281)
        self.hideturtle()
        with open("day20/high_score.txt",mode = "r") as file:
                if(file.read().isdigit()):
                    self.high_score = int(file.read())
                else:
                    self.high_score = 0
        
    def print_score(self, score):
        self.clear()
        self.write(f"Score : {score}    High Score: {self.high_score}",False,"center",("Arial",12,"normal"))
        
    def reset(self, score):
        if score > self.high_score:
            self.high_score = score
            with open("day20/high_score.txt",mode = "w") as file:
                file.write(f"{self.high_score} ")
        self.print_score(0)
        
        