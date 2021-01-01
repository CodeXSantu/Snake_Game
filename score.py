from turtle import Turtle
FONT = ("Courier",22,"normal")
MOVE = False
ALIGNMENT = "center" 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.ht()
        self.update()

    def update(self):
        self.write(f"Score:{self.score}",move=MOVE,align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=MOVE,align=ALIGNMENT,font=FONT)


        
    def new_score(self):
        self.score +=1
        self.clear()
        self.update()




