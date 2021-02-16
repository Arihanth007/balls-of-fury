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
        self.velocity = 1
        self.prev_board = Back.BLACK + ' '
        self.collided_with = None
        pass

    def init_ball(self, play_field):
        play_field[self.start[0]][self.start[1]] = '*'

    def print(self, play_field):
        play_field[self.previous[0]][self.previous[1]] = Back.BLACK + ' '
        play_field[self.current[0]][self.current[1]] = 'ball'

    def check_slider_collision(self, x, y, play_field):
        if self.current[0] >= height-2:
            if play_field[height-2][self.current[1]-1] == '-' or play_field[height-2][self.current[1]+1] == '-':
                self.next[0] -= x
                self.next[1] += y
                return True
            else:
                return False
        else:
            return True

    def check_wall_collision(self, x, y):
        if self.current[0] + x > 1 and self.current[0] + x < height-1:
            self.next[0] += x
        else:
            self.next[0] -= x
        if self.current[1] + y > 1 and self.current[1] + y < width-1:
            self.next[1] += y
        else:
            self.next[1] -= y

    def check_obstacle_collision(self, x, y, play_field, blocks):
        for block in blocks:
            if self.next[0]+x == block[0] and self.next[1]+y == block[1]:
                self.next[0] -= x
                self.next[1] -= y
                self.collided_with = block
                return True
            elif self.next[0]+x == block[0] and self.next[1] == block[1]:
                self.next[0] -= x
                self.next[1] += y
                self.collided_with = block
                return True
            elif self.next[1]+y == block[1] and self.next[0] == block[0]:
                self.next[0] += x
                self.next[1] -= y
                self.collided_with = block
                return True

        return False

    def set_state(self, play_field, blocks):
        x = self.velocity
        y = self.velocity
        if self.current[0] - self.previous[0] < 0:
            x *= -1
        if self.current[1] - self.previous[1] < 0:
            y *= -1
        print(x, y)

        if not self.check_slider_collision(x, y, play_field):
            return False

        if not self.check_obstacle_collision(x, y, play_field, blocks):
            self.check_wall_collision(x, y)
            self.collided_with = None

        self.prev_board = play_field[self.previous[0]][self.previous[1]]
        self.previous = [self.current[0], self.current[1]]
        self.current = [self.next[0], self.next[1]]

        return True
