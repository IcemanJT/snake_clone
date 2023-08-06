#
#     Jeremi Torój 1.08.2023
#

from turtle import Screen
import turtle
from snake import Snake
from fruit import Fruit
from score_board import ScoreBoard
import time
import map


def snake_turn():
    screen.onkeypress(player.up, "Up")
    screen.update()
    screen.onkeypress(player.down, "Down")
    screen.update()
    screen.onkeypress(player.left, "Left")
    screen.update()
    screen.onkeypress(player.right, "Right")
    screen.update()


def snake_eats_fruit():
    if player.snake[0].distance(apple) < 10:
        apple.change_pos()
        player.grow()
        score_board.score += 1
        score_board.write_score()
    for snake_part in player.snake:
        if apple.distance(snake_part) < 10:
            apple.change_pos()


screen = Screen()
screen.setup(width=610, height=640)
screen.setworldcoordinates(0, 0, 610, 640)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")


game_on = False


user_grid_choice = screen.textinput(title="Grid of a map", prompt="Do you want to see the grid? (y/n)")
while user_grid_choice != "y" and user_grid_choice != "n":
    user_grid_choice = screen.textinput(title="Grid of a map", prompt="Do you want to see the grid? (y/n)")

if user_grid_choice == "y":
    map.draw_grid()
    map.draw_map()
else:
    map.draw_map()

screen.update()


while True:
    try:
        player_color_choice = screen.textinput(title="Snake color", prompt="Use arrows to navigate the "
                                                                           "snake to the fruit. \nDuring the game "
                                                                           "make sure"
                                                                           " to not hold the arrows as it bugs snake "
                                                                           "movement\n\nChoose the color of your "
                                                                           "snake.\n"
                                                                           "Color could be anything from the "
                                                                           "https://cs111.wellesley.edu/reference"
                                                                           "/colors,\nwhich contains most of regular "
                                                                           "colors if you dont bother checking\n"
                                                                           "If color is set to random snake is going to"
                                                                           "be colorful.""")
        player = Snake(player_color_choice)
        game_on = True
        break
    except (turtle.TurtleGraphicsError, TypeError):
        while screen.textinput(title="Error", prompt="Wrong input. Try again. Write \"ok\".") != "ok":
            continue


apple = Fruit()
score_board = ScoreBoard()


while game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    snake_turn()
    snake_eats_fruit()
    screen.update()
    time.sleep(0.1)
    player.move()
    snake_eats_fruit()
    if not player.is_alive:
        if len(player.snake) >= 30 * 28:
            map.draw_win()
            screen.update()
            game_on = False
            continue
        else:
            map.draw_lose()
            screen.update()
            game_on = False
            continue

screen.exitonclick()
