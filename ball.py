import numpy as np
from time import clock_getres, sleep
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Ball:

    def __init__(self):
        self.start = [height-3, int(width/2)]
        self.previous = [self.start[0]+1, self.start[1]+1]
        self.current = [self.start[0], self.start[1]]
        self.next = [self.start[0], self.start[1]]
        self.x_velocity = 1
        self.y_velocity = 1
        self.collided_with = None
        self.power_up_collision = False

    def init_ball(self, play_field):
        play_field[self.start[0]][self.start[1]] = 'ball'

    def print(self, play_field):
        play_field[self.previous[0]][self.previous[1]] = Back.BLACK + ' '
        play_field[self.current[0]][self.current[1]] = 'ball'

    def place_ball(self, play_field, slider_dimensions):
        slider_width = slider_dimensions[1] - slider_dimensions[0]
        slider_mid = int(slider_dimensions[1] - (slider_width/2))

        t = slider_mid-self.current[1]
        if t != 0:
            play_field[self.current[0]][self.current[1]] = Back.BLACK + ' '
            self.current[1] += t
            self.next[1] += t
            self.previous[1] += t
            play_field[self.current[0]][self.current[1]] = 'ball'
            self.start[1] = self.current[1]

    def increase_speed(self):
        self.x_velocity = 2
        self.y_velocity = 2

    def pass_through_blocks(self):
        self.power_up_collision = True

    def check_slider_collision(self, x, y, play_field, slider_dimensions):
        slider_width = slider_dimensions[1] - slider_dimensions[0]
        slider_mid = int(slider_dimensions[1] - (slider_width/2))

        if self.current[0] >= height-1-x:
            if self.current[1]+y >= slider_dimensions[0] and self.current[1]+y <= slider_dimensions[1]:
                self.y_velocity = 1 + np.abs(
                    slider_width-(self.current[1]-y)) % 3
                if y < 0:
                    y = -self.y_velocity
                else:
                    y = self.y_velocity
                self.next[0] -= x
                if (y > 0 and self.current[1]+y <= slider_mid) or (y < 0 and self.current[1]+y >= slider_mid):
                    self.next[1] -= y
                else:
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
        X_collision = False
        Y_collision = False

        collision_box = []
        for i in range(min(self.next[0], self.next[0]+x), max(self.next[0], self.next[0]+x)+1):
            for j in range(min(self.next[1], self.next[1]+y), max(self.next[1], self.next[1]+y)+1):
                collision_box.append([i, j])

        for block in blocks:
            if [block[0], block[1]] in collision_box:
                X_collision = True
                Y_collision = True

                if self.next[0] == block[0]:
                    X_collision = False
                if self.next[1] == block[1]:
                    Y_collision = False

                self.collided_with = [block]
                if block[2] == 'yellow':
                    for bl in blocks:
                        if bl[2] == 'yellow' and bl != block:
                            self.collided_with.append(bl)
                    for bl in blocks:
                        if bl[2] != 'yellow':
                            for powerup_block in self.collided_with:
                                if (bl[0] == powerup_block[0]+1 or bl[0] == powerup_block[0]-1) and (bl[1] == powerup_block[1]+1 or bl[1] == powerup_block[1]-1):
                                    self.collided_with.append(bl)

        if (X_collision or Y_collision) and self.power_up_collision:
            self.next[0] += x
            self.next[1] += y
            return True

        if X_collision and Y_collision:
            self.next[0] -= x
            self.next[1] -= y
        elif X_collision:
            self.next[0] -= x
            self.next[1] += y
        elif Y_collision:
            self.next[0] += x
            self.next[1] -= y
        else:
            return False

        return True

    def set_state(self, play_field, blocks, slider_dimensions):
        x = self.x_velocity
        y = self.y_velocity
        if self.current[0] - self.previous[0] < 0:
            x *= -1
        if self.current[1] - self.previous[1] < 0:
            y *= -1
        print(x, y)

        if self.check_slider_collision(x, y, play_field, slider_dimensions):

            if not self.check_obstacle_collision(x, y, play_field, blocks):
                self.check_wall_collision(x, y)
                self.collided_with = None

            play_field[self.previous[0]][self.previous[1]] = Back.BLACK + ' '
            self.previous = [self.current[0], self.current[1]]
            self.current = [self.next[0], self.next[1]]
            return True

        return False
