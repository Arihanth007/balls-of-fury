import os
from time import sleep
import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Slider:

    def init_slider(self, play_field):
        self.slider_width = np.array([width/2-8, width/2+8], dtype=int)
        self.slider_height = height-2

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

    def print_slider(self, val, play_field):
        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = ' '

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
