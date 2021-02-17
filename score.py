import numpy as np
from time import clock_getres, sleep
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Score:

    def __init__(self) -> None:
        self.score = 0
        self.time = 0
        self.lives = 1
        self.output = 'Score: {}, Time: {}, Lives: {}'.format(
            self.score, self.time, self.lives)

    def update_score(self, count, tme, lives, play_field):
        self.score += count
        self.time += tme
        self.lives = lives
        self.output = 'Score: {}, Time: {}, Lives: {}'.format(
            self.score, self.time, self.lives)
        for i in range(height):
            for j in range(width):
                if j < len(self.output):
                    play_field[i][j] = self.output[j]
                else:
                    break
            break
