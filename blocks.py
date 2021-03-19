from config import height, width, black, red, green, blue
import random


class Blocks:

    def __init__(self, strength, color):
        self.blocks = []  # stores all present blocks
        self.strength = strength
        self.color = color

    # reduces the strength of the ball
    # ball is removed based on strength
    def reduce_block_strength(self, block, play_field, num):

        # erases it from being displayed to avoid glitches
        # it is added back by the refresh_blocks function
        play_field[block[0]][block[1]] = black
        for index, bl in enumerate(self.blocks):
            if bl == block:
                self.blocks.remove(bl)

    # intializes the block positions
    def init_blocks(self, play_field, num, row):

        # not actually random lol
        cords = self.__generate_random_pattern(num, row)

        # checks for some cases
        # appends all blocks to the array
        for cord in cords:
            play_field[cord[0] % height][cord[1]] = self.color
            self.blocks.append(
                [cord[0] % height, cord[1], self.color, self.strength])

    # generates the block patter
    def __generate_random_pattern(self, num, row):
        return [[row, (i*int((width-10)/num)+10)] for i in range(num)]

    # resets the display of the blocks to avoid glitches
    def refresh_blocks(self, play_field):
        for block in self.blocks:
            play_field[block[0]][block[1]] = block[2]

    # resets all blocks on screen
    def clear_all(self, playfield):
        for block in self.blocks:
            playfield[block[0]][block[1]] = black
        self.blocks.clear()

    # block moves down by 1
    def push_down(self, playfield):
        for index, bl in enumerate(self.blocks):
            playfield[bl[0]][bl[1]] = black
            self.blocks[index][0] = bl[0]+1
        self.refresh_blocks(playfield)


# example of inheritance
class GreenBlocks(Blocks):
    pass

# example of inheritance


class RedBlocks(Blocks):
    pass

# example of inheritance


class BlueBlocks(Blocks):
    pass

# example of inheritance


class IndestructibleBlocks(Blocks):
    # reduces the strength of the ball
    # ball is removed based on strength
    def reduce_block_strength(self, block, play_field, num):

        # erases it from being displayed to avoid glitches
        # it is added back by the refresh_blocks function
        play_field[block[0]][block[1]] = black
        for index, bl in enumerate(self.blocks):
            # This logic was built
            # when blocks didn't change color
            if bl[3]-num <= 0:
                self.blocks.remove(bl)
            else:
                self.blocks[index][3] -= num

# example of inheritance
# and polymorphism


class PowerupBlocks(Blocks):

    # polymorphism
    # it genrates blocks side-by-side
    def init_blocks(self, play_field, num, row):

        # all exploding blocks
        # are next to each other
        cords = [[row, int(width/2)-int(num/2)+i] for i in range(num)]

        # these are added to the array
        for cord in cords:
            play_field[cord[0] % height][cord[1]] = self.color
            self.blocks.append(
                [cord[0] % height, cord[1], self.color, self.strength])


class RainbowBlocks(Blocks):

    def __init__(self):
        self.blocks = []  # stores all present blocks

    # intializes the block positions
    def init_blocks(self, play_field, num, row):

        # not actually random lol
        cords = [[row, (i*int((width-10)/num)+10)] for i in range(num)]
        color = ['blue', 'green', 'red']

        # checks for some cases
        # appends all blocks to the array
        for cord in cords:
            strength = random.choice([1, 2, 3])
            play_field[cord[0] % height][cord[1]] = color[strength-1]
            self.blocks.append(
                [cord[0] % height, cord[1], color[strength-1], strength])

    # color, strength keeps changing
    # until collided with
    def rainbow_effect(self):

        # keeps track of color
        # index+1 = strength of the color
        color = ['blue', 'green', 'red']

        # randomly change colors
        for index, bl in enumerate(self.blocks):
            strength = random.choice([1, 2, 3])
            self.blocks[index][2] = color[strength-1]
            self.blocks[index][3] = strength
