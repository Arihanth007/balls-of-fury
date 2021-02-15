import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Ball:

    def __init__(self) -> None:
        self.start = [height-3, int(width/2)]
        self.end = [0, 0]
        self.previous = [self.start[0]+1, self.start[1]+1]
        self.current = [self.start[0], self.start[1]]
        self.next = [self.start[0], self.start[1]]
        pass

    def init_ball(self, play_field):
        play_field[self.start[0]][self.start[1]] = '*'

    def print(self, play_field):
        play_field[self.previous[0]][self.previous[1]] = ' '
        play_field[self.current[0]][self.current[1]] = '*'

    def check_wall_collision(self, x, y):
        if self.current[0] + x > 1 and self.current[0] + x < height-1:
            self.next[0] += x
        else:
            self.next[0] -= x
        if self.current[1] + y > 1 and self.current[1] + y < width-3:
            self.next[1] += y
        else:
            self.next[1] -= y

    def check_obstacle_collision(self, x, y, play_field):
        if play_field[self.next[0]-1][self.next[1]] != ' ' or play_field[self.next[0]+1][self.next[1]] != ' ':
            self.next[0] -= x
            self.next[1] += y
            return True
        if play_field[self.next[0]][self.next[1]-1] != ' ' or play_field[self.next[0]][self.next[1]+1] != ' ':
            self.next[0] += x
            self.next[1] -= y
            return True

        return False

    def set_state(self, play_field):
        x = self.current[0] - self.previous[0]
        y = self.current[1] - self.previous[1]

        if not self.check_obstacle_collision(x, y, play_field):
            self.check_wall_collision(x, y)

        self.previous = [self.current[0], self.current[1]]
        self.current = [self.next[0], self.next[1]]
