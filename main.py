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


def snake_turn(head, window):
    window.onkeypress(head.up, "Up")
    window.update()
    window.onkeypress(head.down, "Down")
    window.update()
    window.onkeypress(head.left, "Left")
    window.update()
    window.onkeypress(head.right, "Right")
    window.update()


def snake_eats_fruit(fruit, player_head, scoreboard):
    if player_head.snake[0].distance(fruit) < 10:
        fruit.change_pos()
        player_head.grow()
        scoreboard.score += 1
        scoreboard.write_score()
    for snake_part in player_head.snake:
        if fruit.distance(snake_part) < 10:
            fruit.change_pos()


def make_grid(canvas):
    user_grid_choice = canvas.textinput(title="Grid of a map", prompt="Do you want to see the grid? (y/n)")
    while user_grid_choice != "y" and user_grid_choice != "n" and user_grid_choice != "":
        user_grid_choice = canvas.textinput(title="Grid of a map", prompt="Do you want to see the grid? (y/n)")
    if user_grid_choice == "y":
        map.draw_grid()
        map.draw_map()
    elif user_grid_choice == "n" or user_grid_choice == "":
        map.draw_map()


def screen_setup():
    canvas = Screen()
    canvas.setup(width=610, height=640)
    canvas.setworldcoordinates(0, 0, 610, 640)
    canvas.tracer(0)
    canvas.bgcolor("black")
    canvas.title("Snake Game")
    make_grid(canvas)
    map.draw_reset_quit()
    return canvas


def breaker():
    global playing
    playing = False


def player_setup(pop_up):
    while True:
        try:
            player_color_choice = pop_up.textinput(title="Snake color", prompt=""
                                                                               "Use arrows to navigate the "
                                                                               "snake to the fruit. \nDuring the game "
                                                                               "make sure "
                                                                               "to not hold the arrows as it bugs the "
                                                                               "snake's"
                                                                               "movement\n\nChoose the color of your "
                                                                               "snake.\n"
                                                                               "Color could be anything from the "
                                                                               "https://cs111.wellesley.edu/reference"
                                                                               "/colors,\nwhich contains most of "
                                                                               "regular "
                                                                               "colors if you dont bother checking.\n"
                                                                               "If color is set to random snake is "
                                                                               "going to "
                                                                               "be colorful.""")
            snake = Snake(player_color_choice)
            return snake
        except (turtle.TurtleGraphicsError, TypeError):
            while pop_up.textinput(title="Error", prompt="Wrong input. Try again. Write \"ok\".") != "ok":
                continue


playing = True


def game(board, snake, sweet, scoreboard):
    board.onkey(breaker, "q")
    while playing:
        board.listen()
        board.update()
        time.sleep(0.1)
        snake_turn(head=snake, window=board)
        snake_eats_fruit(fruit=sweet, player_head=snake, scoreboard=scoreboard)
        board.update()
        time.sleep(0.1)
        snake.move()
        snake_eats_fruit(fruit=sweet, player_head=snake, scoreboard=scoreboard)
        if not snake.is_alive:
            if len(snake.snake) >= 30 * 28:
                map.draw_win()
                break
            else:
                map.draw_lose()
                break


while True:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
    screen = screen_setup()
    apple = Fruit()
    score_board = ScoreBoard(high_score)
    player = player_setup(screen)
    game(board=screen, snake=player, sweet=apple, scoreboard=score_board)
    user_choice = screen.textinput(title="Game over", prompt="Do you want to play again? (y/n)")
    while user_choice != "y" and user_choice != "n" and user_choice != "":
        user_choice = screen.textinput(title="Game over", prompt="Do you want to play again? (y/n)")
    if user_choice == "y":
        screen.clear()
        score_board.reset()
        continue
    elif user_choice == "n" or user_choice == "":
        screen.bye()
        score_board.reset()
        break
