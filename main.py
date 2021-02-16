import numpy as np
from screen import Screen, display
from slider import Slider
from blocks import GreenBlocks, RedBlocks, BlueBlocks, IndestructibleBlocks
from ball import Ball
from input import getInput
from input import input_to

screen = Screen(30, 79)
slider = Slider()
blue_blocks = BlueBlocks(1, 'blue')
green_blocks = GreenBlocks(2, 'green')
red_blocks = RedBlocks(3, 'red')
indestructible_blocks = IndestructibleBlocks(np.inf, 'yellow')
ball = Ball()
key_input = getInput()

slider.init_slider(screen.play_field)
red_blocks.init_blocks(screen.play_field, 10, 5)
green_blocks.init_blocks(screen.play_field, 10, 7)
blue_blocks.init_blocks(screen.play_field, 10, 10)
indestructible_blocks.init_blocks(screen.play_field, 1, 13)
ball.init_ball(screen.play_field)

time_elapsed = 0.1
isTrue = True

display(screen.play_field)
ball.print(screen.play_field)
while key_input.__call__() != 'p':
    pass


def refresh_all_blocks():
    green_blocks.refresh_blocks(screen.play_field)
    red_blocks.refresh_blocks(screen.play_field)
    blue_blocks.refresh_blocks(screen.play_field)
    indestructible_blocks.refresh_blocks(screen.play_field)


def update_block_strength():
    color = ball.collided_with[2]
    if color == 'green':
        green_blocks.reduce_block_strength(
            ball.collided_with, screen.play_field)
    elif color == 'red':
        red_blocks.reduce_block_strength(
            ball.collided_with, screen.play_field)
    elif color == 'blue':
        blue_blocks.reduce_block_strength(
            ball.collided_with, screen.play_field)


def combine_all_blocks():
    all_blocks = []
    for block in green_blocks.blocks:
        all_blocks.append(block)
    for block in red_blocks.blocks:
        all_blocks.append(block)
    for block in blue_blocks.blocks:
        all_blocks.append(block)
    for block in indestructible_blocks.blocks:
        all_blocks.append(block)
    return all_blocks


def main():
    display(screen.play_field)

    all_blocks = combine_all_blocks()
    isTrue = ball.set_state(screen.play_field, all_blocks)
    ball.print(screen.play_field)
    if ball.collided_with is not None:
        update_block_strength()
        print('Removed')
    refresh_all_blocks()
    return isTrue


while main():
    key_pressed = key_input.__call__()
    # key_pressed = input_to(key_input.__call__)
    if key_pressed == 'q':
        break
    slider.move(screen.play_field, key_pressed)
    pass
