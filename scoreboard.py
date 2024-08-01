from turtle import Turtle
"""Making value for alignment and font"""
Alignment = "center"
font = ("Arial",10,"normal")

"""Making scoreboard child class of turtle"""
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        """Making attributes for score"""
        self.score = 0
        with open('Data.txt','r') as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        """Making turtle position fixed"""
        self.goto(0,270)
        """Hiding Turtle"""
        self.hideturtle()
        self.update_scoreboard()

    """Making function called update_scoreboard"""
    def update_scoreboard(self):
        """Write function to write score"""
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=Alignment, font=font)

    """Making new function called game_over"""
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Data.txt','w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

        """Making function called increase_store"""
    def increase_score(self):

        self.score += 1
        """Calling clear function to clear which is already written"""
        self.clear()
        """Calling update_scoreboard"""
        self.update_scoreboard()

