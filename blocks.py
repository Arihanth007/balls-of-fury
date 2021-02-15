import os
from time import sleep
import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from screen import Screen
from config import block_size, height, width


class Blocks:

    def __init__(self):
        self.block_size = block_size

    def init_blocks(self, play_field):
        def set_blocks(num, color):
            cords = self.generate_pattern(num)
            for cord in cords:
                play_field[cord[0] % height][cord[1]] = color + ' '
                play_field[cord[0] % height][cord[1]+1] = Back.BLACK + ' '

        set_blocks(50, Back.GREEN)
        set_blocks(50, Back.BLUE)
        set_blocks(50, Back.RED)

    def generate_pattern(self, num):
        cords = []
        for i in range(num):
            cords.append([np.random.randint(5, height-10),
                          np.random.randint(10, width-10)])

        return cords
