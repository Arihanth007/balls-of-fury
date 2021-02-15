import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from screen import display
from config import height, width


class Ball:

    def __init__(self) -> None:
        self.start = [height-3, int(width/2)]
        self.end = [0, 0]
        self.current = self.start
        self.next = [0, 0]
        pass

    def init_ball(self, play_field):
        play_field[self.start[0]][self.start[1]] = '*'

    def track_ball(self, play_field):
        pass

    def set_direction(self):
        pass
