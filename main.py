import numpy as np
from screen import Screen, display
from slider import Slider
from blocks import GreenBlocks, RedBlocks, BlueBlocks, IndestructibleBlocks, PowerupBlocks
from ball import Ball
from input import getInput
from input import input_to

screen = Screen(30, 79)
slider = Slider()
blue_blocks = BlueBlocks(1, 'blue')
green_blocks = GreenBlocks(2, 'green')
red_blocks = RedBlocks(3, 'red')
indestructible_blocks = IndestructibleBlocks(1, 'white')
powerup_blocks = PowerupBlocks(1, 'yellow')
ball = Ball()
key_input = getInput()

slider.init_slider(screen.play_field)
indestructible_blocks.init_blocks(screen.play_field, 5, 2)
red_blocks.init_blocks(screen.play_field, 10, 5)
powerup_blocks.init_blocks(screen.play_field, 50, 11)
green_blocks.init_blocks(screen.play_field, 10, 7)
blue_blocks.init_blocks(screen.play_field, 10, 10)
ball.init_ball(screen.play_field)

time_elapsed = 0.1
isTrue = True

display(screen.play_field)
ball.print(screen.play_field)

print('Adjust the board and press P to start the game')
k_press = 'notPlol'
while k_press != 'p':
    slider.move(screen.play_field, k_press)
    ball.place_ball(screen.play_field, [
                    slider.slider_width[0], slider.slider_width[1]])
    k_press = key_input.__call__()
    pass


def refresh_all_blocks():
    green_blocks.refresh_blocks(screen.play_field)
    red_blocks.refresh_blocks(screen.play_field)
    blue_blocks.refresh_blocks(screen.play_field)
    indestructible_blocks.refresh_blocks(screen.play_field)


def update_block_strength():
    for block in ball.collided_with:
        color = block[2]
        if color == 'green':
            green_blocks.reduce_block_strength(
                block, screen.play_field)
        elif color == 'red':
            red_blocks.reduce_block_strength(
                block, screen.play_field)
        elif color == 'blue':
            blue_blocks.reduce_block_strength(
                block, screen.play_field)
        elif color == 'yellow':
            powerup_blocks.reduce_block_strength(
                block, screen.play_field)


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
    for block in powerup_blocks.blocks:
        all_blocks.append(block)
    return all_blocks


def main():
    display(screen.play_field)

    all_blocks = combine_all_blocks()
    isTrue = ball.set_state(screen.play_field, all_blocks, [
                            slider.slider_width[0], slider.slider_width[1]])
    ball.print(screen.play_field)
    if ball.collided_with is not None:
        update_block_strength()
    refresh_all_blocks()
    return isTrue


while main():
    # key_pressed = key_input.__call__()
    key_pressed = input_to(key_input.__call__)
    if key_pressed == 'q':
        break
    slider.move(screen.play_field, key_pressed)
    pass
