#
# Jeremi Torój 5.08.2023
#

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, high_score):
        super().__init__(visible=False)
        self.penup()
        self.speed(0)
        self.color("white")
        self.score = 0
        self.high_score = high_score
        self.setpos(10, 610)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
