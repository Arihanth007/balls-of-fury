import os
from time import sleep
from time import time

from numpy.core.shape_base import block
from screen import Screen, display
from slider import Slider
from blocks import Blocks
from ball import Ball
from input import getInput

screen = Screen(30, 79)
slider = Slider()
blocks = Blocks()
ball = Ball()
key_input = getInput()

slider.init_slider(screen.play_field)
blocks.init_blocks(screen.play_field)
ball.init_ball(screen.play_field)

time_elapsed = 0.1


def main():
    display(screen.play_field)

    key_pressed = key_input.__call__()
    if key_pressed == 'q':
        return False
    slider.move(screen.play_field, key_pressed)

    return True


while main():
    # sleep(0.2)
    pass
