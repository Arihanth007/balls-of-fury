import os
from time import sleep
from time import time

from numpy.core.shape_base import block
from screen import Screen, display
from slider import Slider
from blocks import Blocks
from ball import Ball
from input import getInput
from input import input_to

screen = Screen(30, 79)
slider = Slider()
blocks = Blocks()
ball = Ball()
key_input = getInput()

slider.init_slider(screen.play_field)
blocks.init_blocks(screen.play_field)
ball.init_ball(screen.play_field)

time_elapsed = 0.1
isTrue = True

display(screen.play_field)
ball.print(screen.play_field)
while key_input.__call__() != 'p':
    pass


def main():
    display(screen.play_field)

    isTrue = ball.set_state(screen.play_field, blocks.blocks)
    ball.print(screen.play_field)
    if ball.collided_with is not None:
        blocks.reduce_block_strength(ball.collided_with, screen.play_field)
        print('Removed')
    blocks.refresh_blocks(screen.play_field)

    return isTrue


while main():
    key_pressed = key_input.__call__()
    # key_pressed = input_to(key_input.__call__)
    if key_pressed == 'q':
        break
    slider.move(screen.play_field, key_pressed)
    pass
