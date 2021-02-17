import numpy as np
from time import clock_getres, sleep
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Powerup:

    def init_powerup(self, x, y):
        self.start = [x, y]
        self.previous = [self.start[0], self.start[1]]
        self.current = [self.start[0], self.start[1]]
        self.x_velocity = 1
        self.collided_with = None

    def print(self, play_field):
        if self.current[0] < height-2:
            play_field[self.previous[0]][self.previous[1]] = Back.BLACK + ' '
            play_field[self.current[0]][self.current[1]] = 'powerup'
        elif self.current[0] > height-2 and self.current[0] < height:
            play_field[self.previous[0]-3][self.previous[1]] = Back.BLACK + ' '
            play_field[self.current[0]-3][self.current[1]] = Back.BLACK + ' '
            play_field[self.previous[0]-2][self.previous[1]] = Back.BLACK + ' '
            play_field[self.current[0]-2][self.current[1]] = Back.BLACK + ' '
            # play_field[self.previous[0]][self.previous[1]] = Back.BLACK + ' '
            # play_field[self.current[0]][self.current[1]] = Back.BLACK + ' '
            self.previous = [np.inf, np.inf]
            self.current = [np.inf, np.inf]

    def check_slider_collision(self, play_field, slider_dimensions):
        if self.current[0] >= height-1-self.x_velocity and self.current[0] < height:
            if self.current[1] >= slider_dimensions[0] and self.current[1] <= slider_dimensions[1]:
                play_field[self.previous[0]
                           ][self.previous[1]] = Back.BLACK + ' '
                play_field[self.current[0]][self.current[1]] = Back.BLACK + ' '
                return True
            else:
                return False
        else:
            return False

    def set_state(self, play_field, slider_dimensions):
        if self.check_slider_collision(play_field, slider_dimensions):
            return True
        self.previous[0] = self.current[0]
        self.current[0] += 1
        return False

    def simulation(self, play_field, slider_dimensions):
        if self.current[0] >= height-1:
            return False

        temp = self.set_state(play_field, slider_dimensions)
        if not temp:
            self.print(play_field)
        return temp
