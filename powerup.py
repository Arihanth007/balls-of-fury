import numpy as np
from time import clock_getres, sleep
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Powerup:

    def __init__(self) -> None:
        self.start = None
        self.previous = None
        self.current = None
        self.x_velocity = 1
        self.array_of_powerups = [False]*6
        self.temp = []
        for i in range(len(self.array_of_powerups)):
            t = [False]*6
            t[i] = not(t[i])
            self.temp.append(t)

    def init_powerup(self, x, y):
        self.start = [x, y]
        self.previous = [self.start[0], self.start[1]]
        self.current = [self.start[0]+1, self.start[1]]

    def simulate_powerup(self, play_field, slider_dimensions):
        if self.start is not None:
            if self.current[0] < height-2:
                play_field[self.current[0]][self.current[1]] = 'powerup'
                play_field[self.previous[0]
                           ][self.previous[1]] = Back.BLACK + ' '
                self.previous[0] += 1
                self.current[0] += 1
            else:
                play_field[self.current[0]][self.current[1]] = Back.BLACK + ' '
                play_field[self.previous[0]
                           ][self.previous[1]] = Back.BLACK + ' '
                self.start = None
                if self.current[1] >= slider_dimensions[0] and self.current[1] <= slider_dimensions[1]:
                    return self.temp[np.random.randint(1, 6)]

        return self.array_of_powerups
