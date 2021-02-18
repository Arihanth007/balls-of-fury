import os
import numpy as np
from config import height, width, red, green, blue, yellow, white, magenta, black


def display(play_field):
    os.system('clear')
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


def flush_display(play_field):
    for i in range(height):
        for j in range(width):
            if play_field[i][j] == 'ball':
                play_field[i][j] = black


class Screen:
    ''' Display home screen '''

    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.play_field = np.array([[black for j in range(
            self.width)] for i in range(self.height)], dtype='object')

        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width-1:
                    self.play_field[i][j] = '|'
                if i == 0 or i == self.height-1:
                    self.play_field[i][j] = '_'
