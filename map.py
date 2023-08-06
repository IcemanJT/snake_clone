#
# Jeremi Torój 1.08.2023
#

from turtle import Turtle


def draw_grid():
    grid = Turtle()
    grid.hideturtle()
    grid.speed(0)
    grid.color("grey")
    grid.pensize(1)
    for j in range(20, 581, 20):
        grid.penup()
        grid.setpos(x=j, y=0)
        grid.pendown()
        grid.setheading(90)
        grid.forward(600)
    for k in range(20, 581, 20):
        grid.penup()
        grid.setpos(x=0, y=k)
        grid.pendown()
        grid.setheading(0)
        grid.forward(600)


def draw_map():
    map_pen = Turtle(visible=False)
    map_pen.speed(0)
    map_pen.pensize(3)
    map_pen.color("white")
    for h in range(0, 601, 600):
        map_pen.penup()
        map_pen.setpos(x=h, y=0)
        map_pen.pendown()
        map_pen.setheading(90)
        map_pen.forward(600)
    for b in range(0, 601, 600):
        map_pen.penup()
        map_pen.setpos(x=0, y=b)
        map_pen.pendown()
        map_pen.setheading(0)
        map_pen.forward(600)


def draw_win():
    win = Turtle(visible=False)
    win.speed(0)
    win.color("Yellow")
    win.pensize(5)
    win.penup()
    win.setpos(x=300, y=400)
    win.write("You win!", align="center", font=("Arial", 50, "normal"))


def draw_lose():
    lose = Turtle(visible=False)
    lose.speed(0)
    lose.color("red")
    lose.pensize(5)
    lose.penup()
    lose.setpos(x=300, y=400)
    lose.write("You lose!", align="center", font=("Arial", 50, "normal"))
