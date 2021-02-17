import os
from time import sleep
import numpy as np
from colorama import Fore, Back, Style
from input import getInput
from screen import Screen
from config import block_size, height, width


class Blocks:

    def __init__(self, strength, color):
        self.block_size = block_size
        self.blocks = []
        self.strength = strength
        self.color = color

    def reduce_block_strength(self, block, play_field):
        play_field[block[0]][block[1]] = Back.BLACK + ' '
        for index, bl in enumerate(self.blocks):
            if bl == block:
                if bl[3] <= 1:
                    self.blocks.remove(bl)
                else:
                    self.blocks[index][3] -= 1

    def init_blocks(self, play_field, num, row):
        cords = self.generate_random_pattern(num, row)
        for cord in cords:
            play_field[cord[0] % height][cord[1]] = self.color
            self.blocks.append(
                [cord[0] % height, cord[1], self.color, self.strength])

    def generate_random_pattern(self, num, row):
        cords = []
        for i in range(num):
            # cords.append([row, (i*2+10)])
            cords.append([row, (i*6+10)])
        # for i in range(num):
        #     cords.append([np.random.randint(row, row+1),
        #                   np.random.randint(10, width-10)])
        return cords

    def refresh_blocks(self, play_field):
        for block in self.blocks:
            play_field[block[0]][block[1]] = block[2]


class GreenBlocks(Blocks):
    pass


class RedBlocks(Blocks):
    pass


class BlueBlocks(Blocks):
    pass


class IndestructibleBlocks(Blocks):
    pass

    # class Blocks:

    #     def __init__(self, strength, color):
    #         self.block_size = block_size
    #         self.blocks = []
    #         self.strength = strength
    #         self.color = color

    #     def reduce_block_strength(self, block, play_field):
    #         play_field[block[0]][block[1]] = Back.BLACK + ' '
    #         for index, bl in enumerate(self.blocks):
    #             if bl == block:
    #                 if bl[3] == 1:
    #                     self.blocks.remove(bl)
    #                 else:
    #                     self.blocks[index][3] -= 1

    #     def init_blocks(self, play_field):
    #         def set_blocks(num, color, row):
    #             cords = self.generate_random_pattern(num, row)
    #             for cord in cords:
    #                 play_field[cord[0] % height][cord[1]] = color
    #                 self.blocks.append(
    #                     [cord[0] % height, cord[1], color, self.strength])

    #         set_blocks(10, 'green', 7)
    #         set_blocks(10, 'blue', 10)
    #         set_blocks(10, 'red', 5)

    #     def generate_random_pattern(self, num, row):
    #         cords = []
    #         for i in range(num):
    #             cords.append([np.random.randint(row, row+1),
    #                           np.random.randint(10, width-10)])

    #         return cords

    #     def refresh_blocks(self, play_field):
    #         for block in self.blocks:
    #             play_field[block[0]][block[1]] = block[2]
