import os
from time import sleep

from numpy.core.shape_base import block
from screen import Screen, display
from slider import Slider
from blocks import Blocks

screen = Screen(30, 79)
slider = Slider()
blocks = Blocks()

slider.init_slider(screen.play_field)
blocks.init_blocks(screen.play_field)

display(screen.play_field)

slider.move(screen.play_field)
