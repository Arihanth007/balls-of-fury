import os
from time import sleep
import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Slider:

    def __init__(self):
        self.swidth = 8

    def init_slider(self, play_field):
        self.slider_width = np.array(
            [int(width/2)-self.swidth, int(width/2)+self.swidth], dtype=int)
        self.slider_height = height-2

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

    def print_slider(self, val, play_field):
        for i in range(1, width-1):
            play_field[self.slider_height][i] = Back.BLACK + ' '

        if val > 0 and self.slider_width[1]+val < width:
            self.slider_width[0] += val
            self.slider_width[1] += val
        if val < 0 and self.slider_width[0]+val > 0:
            self.slider_width[0] += val
            self.slider_width[1] += val

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

        display(play_field)

    def move(self, play_field, key_press):
        if key_press == 'd':
            self.print_slider(1, play_field)
        elif key_press == 'a':
            self.print_slider(-1, play_field)

    def shrink_slider(self, play_field):
        self.swidth = 4
        self.slider_width[0] += 4
        self.slider_width[1] -= 4
        self.init_slider(play_field)

    def expand_slider(self,  play_field):
        self.swidth = 16
        if self.slider_width[0] - 4 <= 1:
            self.slider_width += (self.slider_width[0]-4)
        if self.slider_width[1] + 4 >= width-1:
            self.slider_width += (self.slider_width[1]+4)
        self.slider_width[0] -= 4
        self.slider_width[1] += 4
        self.init_slider(play_field)
