---------------------

# Jeremi Torój 7.08.2023

---------------------

Snake clone.

The entire game was made using only built-in Python libraries, turtle, and random, which means you only need Python installed for it to work properly.

Keep in mind it was made on Linux Ubuntu 22.04.

---------------------

Project contains 5 files:
    3 classes - snake, fruit, and scoreboard
    1 file map.py holding mapping functions for the grid and on-screen text
    1 main.py which contains functions operating on class objects and dependencies between them

---------------------

# Running the game

As I mentioned, you only need Python to play it.

You can run the game in two ways:

1. Create a project, add all the files there, and run "main.py".

or

2. Open a Unix-based terminal in the directory with all the project files and type: 

$python3 main.py

---------------------


---------------------

# Gameplay:

Before the game starts, you will be asked if you want to see the grid of the map.
In my opinion, it helps to navigate the snake, but it's all up to you.

Then a snake customization window will pop up, asking you for a snake color.
All available colors for Python turtle lib are listed here: https://cs111.wellesley.edu/reference/colors

In order to control the snake, use the arrow keys.
Make sure not to hold the keys because it makes the snake move only in one direction until it's done processing a lot of input from the held key.

Avoid walls and the snake's tail.

Navigate the snake to the red dot - the fruit, to grow larger.

If you didn't like your snake customization, you can always hit the "q" button to reset the game, giving you the option to customize the map and snake again.

---------------------



