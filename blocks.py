from config import height, width, black


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
                # This logic was built
                # when blocks didn't change color
                # if bl[3]-num <= 0:
                #     self.blocks.remove(bl)
                # else:
                #     self.blocks[index][3] -= num

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
    pass

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
