import numpy as np
from config import height, width


class GameFlow():

    def __init__(self, screen, slider, ball, second_ball, green_blocks, red_blocks, blue_blocks, indestructible_blocks, powerup_blocks, key_input, isPowerup, isTrue1, isTrue2):
        self.screen = screen
        self.slider = slider
        self.ball = ball
        self.second_ball = second_ball
        self.green_blocks = green_blocks
        self.red_blocks = red_blocks
        self.blue_blocks = blue_blocks
        self.indestructible_blocks = indestructible_blocks
        self.powerup_blocks = powerup_blocks
        self.key_input = key_input
        self.isPowerup = isPowerup
        self.isTrue1 = isTrue1
        self.isTrue2 = isTrue2

    # Player can set the starting release of the ball
    # Press P to release
    def hold_ball(self):

        print('Adjust the board and press P to resume')
        k_press = 'notPlol'

        while k_press != 'p':
            self.slider.move(self.screen.play_field, k_press)
            self.ball.place_ball(self.screen.play_field, [
                self.slider.slider_width[0], self.slider.slider_width[1]])
            k_press = self.key_input.__call__()
            pass

    # Kind of like adding the block
    # to the screen after every iteration
    def refresh_all_blocks(self):
        self.green_blocks.refresh_blocks(self.screen.play_field)
        self.red_blocks.refresh_blocks(self.screen.play_field)
        self.blue_blocks.refresh_blocks(self.screen.play_field)
        self.indestructible_blocks.refresh_blocks(self.screen.play_field)
        self.powerup_blocks.refresh_blocks(self.screen.play_field)

    # Called on collision of ball 1
    # Reduces block strength
    def update_block_strength(self):

        num = 1  # by default

        # if the ball can pass through any block
        if self.ball.power_up_collision:
            num = np.inf

        for block in self.ball.collided_with:
            color = block[2]
            if color == 'green':
                self.green_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'red':
                self.red_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'blue':
                self.blue_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'yellow':
                self.powerup_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'white':
                self.indestructible_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)

    # Called on collision of ball 2
    # Reduces block strength
    def update_second_block_strength(self):

        num = 1  # by default

        # if the ball can pass through any block
        if self.second_ball.power_up_collision:
            num = np.inf

        for block in self.second_ball.collided_with:
            color = block[2]
            if color == 'green':
                self.green_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'red':
                self.red_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'blue':
                self.blue_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'yellow':
                self.powerup_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)
            elif color == 'white':
                self.indestructible_blocks.reduce_block_strength(
                    block, self.screen.play_field, num)

    # Returns an array containing
    # coordinates of all blocks
    def combine_all_blocks(self):

        all_blocks = []
        for block in self.green_blocks.blocks:
            all_blocks.append(block)
        for block in self.red_blocks.blocks:
            all_blocks.append(block)
        for block in self.blue_blocks.blocks:
            all_blocks.append(block)
        for block in self.indestructible_blocks.blocks:
            all_blocks.append(block)
        for block in self.powerup_blocks.blocks:
            all_blocks.append(block)

        return all_blocks

    # Goes through the powerup array
    # calls the respective powerup
    # resets the powerup array
    def check_powerup(self):

        if self.isPowerup[0]:
            self.slider.expand_slider(self.screen.play_field)
            self.isPowerup[0] = False

        if self.isPowerup[1]:
            self.slider.shrink_slider(self.screen.play_field)
            self.isPowerup[1] = False

        if self.isPowerup[2]:
            if self.isTrue1:
                self.isTrue2 = True
                self.second_ball.start = [height-3, int(width/2)]
            self.isPowerup[2] = False

        if self.isPowerup[3]:
            self.ball.increase_speed()
            self.second_ball.increase_speed()
            self.isPowerup[3] = False

        if self.isPowerup[4]:
            self.ball.pass_through_blocks()
            self.second_ball.pass_through_blocks()
            self.isPowerup[4] = False

        if self.isPowerup[5]:
            self.hold_ball()
            self.isPowerup[5] = False
