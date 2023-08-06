#
# Jeremi Torój 5.08.2023
#

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.speed(0)
        self.color("white")
        self.score = 0
        self.setpos(10, 610)
        self.write(f"Score: {self.score}", font=("Arial", 20, "normal"))

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 20, "normal"))
