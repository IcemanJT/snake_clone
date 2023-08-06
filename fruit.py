#
# Jeremi Torój 5.08.2023
#


from turtle import Turtle
from random import randrange


class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("red")
        self.shape("circle")
        self.shapesize(1 / 2)
        self.setpos(randrange(10, 591, 20), randrange(10, 591, 20))
        self.showturtle()

    def change_pos(self):
        self.setpos(randrange(10, 591, 20), randrange(10, 591, 20))
