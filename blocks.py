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
        self.blocks = []

    def init_blocks(self, play_field):
        def set_blocks(num, color, row):
            cords = self.generate_random_pattern(num, row)
            for cord in cords:
                play_field[cord[0] % height][cord[1]] = color + ' '
                play_field[cord[0] % height][cord[1]+1] = Back.BLACK + ' '
                self.blocks.append([cord[0] % height, cord[1]])

        set_blocks(10, Back.GREEN, 7)
        set_blocks(10, Back.BLUE, 10)
        set_blocks(10, Back.RED, 5)

    def generate_random_pattern(self, num, row):
        cords = []
        for i in range(num):
            # cords.append([np.random.randint(5, height-20),
            #               np.random.randint(10, width-10)])
            cords.append([np.random.randint(row, row+1),
                          np.random.randint(10, width-10)])

        return cords
