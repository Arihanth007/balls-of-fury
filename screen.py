import os
import numpy as np
from config import height, width, red, green, blue, yellow, white, magenta, black


# prints the entire 2D array
# displays the playing field
# or game board
def display(play_field):

    # clears the previous output
    # makes it feel continuous
    os.system('clear')

    # some strings have been coded
    # to print verious colors, symbols
    # prints the 2D array
    for i in range(height):
        for j in range(width):
            if play_field[i][j] == 'red':
                print(red, end='')
            elif play_field[i][j] == 'green':
                print(green, end='')
            elif play_field[i][j] == 'blue':
                print(blue, end='')
            elif play_field[i][j] == 'yellow':
                print(yellow, end='')
            elif play_field[i][j] == 'white':
                print(white, end='')
            elif play_field[i][j] == 'ball':
                print('*', end='')
            elif play_field[i][j] == 'powerup':
                print(magenta, end='')
            else:
                print(play_field[i][j], end='')
        print('')


# prints the borders
def set_border(play_field):

    for i in range(height):
        for j in range(width):
            if j == 0 or j == width-1:
                play_field[i][j] = '|'
            if i == 0 or i == height-1:
                play_field[i][j] = '_'


# clears everything
def clear_entire_screen(play_field):

    # clears everything
    for i in range(height):
        for j in range(width):
            play_field[i][j] = black

    # sets borders
    set_border(play_field)


class Screen:
    ''' Display home screen '''

    def __init__(self, height, width):

        # sets dimensions of the screen
        self.height = height
        self.width = width

        # initializes everything to black blocks
        self.play_field = np.array([[black for j in range(
            self.width)] for i in range(self.height)], dtype='object')

        # prints the borders
        set_border(self.play_field)
