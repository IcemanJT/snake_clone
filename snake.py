#
# Jeremi Torój 1.08.2023
#

from turtle import Turtle, colormode
from random import randint

STAMP_SIZE = 20
size = 20


class Snake:

    def __init__(self, color):
        self.snake = []
        self.is_alive = True
        self.x_pos = 310
        self.y_pos = 310
        if color == "":
            self.color = "random"
        else:
            self.color = color
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake_part = Turtle(shape="circle")
            snake_part.hideturtle()
            snake_part.shapesize(size / STAMP_SIZE)
            if self.color == "random":
                colormode(255)
                snake_part.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            else:
                snake_part.color(self.color)
            snake_part.penup()
            snake_part.setpos(x=self.x_pos, y=self.y_pos)
            snake_part.showturtle()
            self.snake.append(snake_part)
            self.x_pos -= 20

    def move(self):
        if not self.is_alive:
            return
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].pos())
        self.snake[0].forward(20)
        self.collision_walls()
        self.collision_body()
        self.snake[-1].showturtle()

    def up(self):
        if self.snake[0].heading() != 270 and self.snake[0].heading() != 90:
            self.snake[0].setheading(90)
            if self.snake[0].ycor() >= 590:
                self.is_alive = False
                return
            self.move()

    def down(self):
        if self.snake[0].heading() != 90 and self.snake[0].heading() != 270:
            self.snake[0].setheading(270)
            if self.snake[0].ycor() <= 10:
                self.is_alive = False
                return
            self.move()

    def left(self):
        if self.snake[0].heading() != 0 and self.snake[0].heading() != 180:
            self.snake[0].setheading(180)
            if self.snake[0].xcor() <= 11:
                self.is_alive = False
                return
            self.move()

    def right(self):
        if self.snake[0].heading() != 180 and self.snake[0].heading() != 0:
            self.snake[0].setheading(0)
            if self.snake[0].xcor() >= 590:
                self.is_alive = False
                return
            self.move()

    def collision_walls(self):
        if self.snake[0].xcor() > 600 or self.snake[0].xcor() < 0 or\
                self.snake[0].ycor() > 600 or self.snake[0].ycor() < 0:
            self.is_alive = False

    def collision_body(self):
        for segment in self.snake[1:]:
            if self.snake[0].position() == segment.position():
                self.is_alive = False

    def grow(self):
        snake_part = Turtle(shape="circle", visible=False)
        snake_part.shapesize(size / STAMP_SIZE)
        if self.color == "random":
            snake_part.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        else:
            snake_part.color(self.color)
        snake_part.penup()
        self.snake.append(snake_part)
