import os
from time import sleep
import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from config import height, width


def display(play_field):
    os.system('clear')
    for i in range(height):
        for j in range(width):
            print(play_field[i][j], end='')
        print('')


class Screen:
    ''' Display home screen '''

    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.play_field = np.array([[' ' for j in range(
            self.width)] for i in range(self.height)], dtype='object')

        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width-1:
                    self.play_field[i][j] = '|'
                if i == 0 or i == self.height-1:
                    self.play_field[i][j] = '_'
