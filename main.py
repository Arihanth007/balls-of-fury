from colorama.ansi import Back
import numpy as np
from time import time
from screen import Screen, display
from slider import Slider
from blocks import GreenBlocks, RedBlocks, BlueBlocks, IndestructibleBlocks, PowerupBlocks
from ball import Ball
from score import Score
from powerup import Powerup
from input import getInput
from input import input_to
from config import height, width, powerups_array
from gameflow import GameFlow


# Creating instances of classes
screen = Screen(30, 79)
slider = Slider()

blue_blocks = BlueBlocks(1, 'blue')
green_blocks = GreenBlocks(2, 'green')
red_blocks = RedBlocks(3, 'red')
indestructible_blocks = IndestructibleBlocks(np.inf, 'white')
powerup_blocks = PowerupBlocks(1, 'yellow')

ball = Ball()
second_ball = Ball()
score = Score()
power_up = Powerup()
key_input = getInput()


# Initializations
slider.init_slider(screen.play_field)

indestructible_blocks.init_blocks(screen.play_field, 15, 2)
red_blocks.init_blocks(screen.play_field, 10, 5)
powerup_blocks.init_blocks(screen.play_field, 50, 6)
green_blocks.init_blocks(screen.play_field, 10, 7)
blue_blocks.init_blocks(screen.play_field, 5, 10)

ball.init_ball(screen.play_field)
display(screen.play_field)
ball.print(screen.play_field)


#  Global variables
isTrue1 = True
isTrue2 = False
isPowerup = powerups_array  # expand, shrink, miltiple, fast, through, grab, powerup
start_time = time()


# Reduces life of primary ball by 1
def update_lives():

    # Creates a new instance of the ball
    global ball
    ball = Ball()

    # Cleares out the previous ball
    screen.play_field[ball.previous[0]][ball.previous[1]] = Back.BLACK + ' '
    screen.play_field[ball.current[0]][ball.current[1]] = Back.BLACK + ' '

    # Initializes the new ball
    ball.init_ball(screen.play_field)
    ball.print(screen.play_field)

    # player can set starting point
    hold_ball()


# Player can set the starting release of the ball
# Press P to release
def hold_ball():

    print('Adjust the board and press P to resume')
    k_press = 'notPlol'
    while k_press != 'p':
        slider.move(screen.play_field, k_press)
        ball.place_ball(screen.play_field, [
                        slider.slider_width[0], slider.slider_width[1]])
        k_press = key_input.__call__()
        pass


# Kind of like adding the block
# to the screen after every iteration
def refresh_all_blocks():
    green_blocks.refresh_blocks(screen.play_field)
    red_blocks.refresh_blocks(screen.play_field)
    blue_blocks.refresh_blocks(screen.play_field)
    indestructible_blocks.refresh_blocks(screen.play_field)
    powerup_blocks.refresh_blocks(screen.play_field)


# Called on collision of ball 1
# Reduces block strength
def update_block_strength():

    num = 1  # by default

    # if the ball can pass through any block
    if ball.power_up_collision:
        num = np.inf

    for block in ball.collided_with:
        color = block[2]
        if color == 'green':
            green_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'red':
            red_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'blue':
            blue_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'yellow':
            powerup_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'white':
            indestructible_blocks.reduce_block_strength(
                block, screen.play_field, num)


# Called on collision of ball 2
# Reduces block strength
def update_second_block_strength():

    num = 1  # by default

    # if the ball can pass through any block
    if second_ball.power_up_collision:
        num = np.inf

    for block in second_ball.collided_with:
        color = block[2]
        if color == 'green':
            green_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'red':
            red_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'blue':
            blue_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'yellow':
            powerup_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'white':
            indestructible_blocks.reduce_block_strength(
                block, screen.play_field, num)


# Returns an array containing
# coordinates of all blocks
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


# Goes through the powerup array
# calls the respective powerup
# resets the powerup array
def check_powerup():

    global isTrue2
    global isPowerup

    if isPowerup[0]:
        slider.expand_slider(screen.play_field)
        isPowerup[0] = False

    if isPowerup[1]:
        slider.shrink_slider(screen.play_field)
        isPowerup[1] = False

    if isPowerup[2]:
        if isTrue1:
            # sets up ball 2 requirements
            isTrue2 = True
            second_ball.start = [height-3, int(width/2)]
        isPowerup[2] = False

    if isPowerup[3]:
        ball.increase_speed()
        second_ball.increase_speed()
        isPowerup[3] = False

    if isPowerup[4]:
        ball.pass_through_blocks()
        second_ball.pass_through_blocks()
        isPowerup[4] = False

    if isPowerup[5]:
        hold_ball()
        isPowerup[5] = False


# Main function that runs the code
def main():

    # Prints the entire screen
    display(screen.play_field)

    # Initialize some variables
    all_blocks = combine_all_blocks()
    global isTrue1
    global isTrue2
    global isPowerup
    slider_dimensions = [slider.slider_width[0], slider.slider_width[1]]

    # Checks if ball 1 is active
    if isTrue1:
        isTrue1 = ball.set_state(
            screen.play_field, all_blocks, slider_dimensions)
        ball.print(screen.play_field)

    # Checks if ball 1 is active
    if isTrue2:
        isTrue2 = second_ball.set_state(
            screen.play_field, all_blocks, slider_dimensions)
        second_ball.print(screen.play_field)

    # Checks for Ball 1 collision with blocks
    if ball.collided_with is not None:
        if 0.3 > np.random.rand() and power_up.start is None:
            # powerups are available
            power_up.init_powerup(
                ball.collided_with[0][0], ball.collided_with[0][1])
        # Update block strength and score
        update_block_strength()
        score.update_score(len(ball.collided_with), int(time() -
                                                        start_time), 0, screen.play_field)
    # Checks for Ball 1 collision with blocks
    if second_ball.collided_with is not None:
        if 0.3 > np.random.rand() and power_up.start is None:
            # powerups are available
            power_up.init_powerup(
                second_ball.collided_with[0][0], second_ball.collided_with[0][1])
        # Update block strength and score
        update_second_block_strength()
        score.update_score(len(second_ball.collided_with), int(time() -
                                                               start_time), 0, screen.play_field)

    # set the powerups randomly
    # if above conditions are met
    isPowerup = power_up.simulate_powerup(
        screen.play_field, slider_dimensions)
    check_powerup()
    refresh_all_blocks()

    # updates score and lives
    score.update_score(0, int(time()-start_time), 0, screen.play_field)
    if not (isTrue1 or isTrue2):
        if score.update_score(
                0, int(time()-start_time), 1, screen.play_field):
            isTrue1 = True
            update_lives()
        display(screen.play_field)

    # continues if either ball is active
    return isTrue1 or isTrue2


# code starts executing from here
# starts from hold position
hold_ball()

# Press q to quit game
while main():

    key_pressed = input_to(key_input.__call__)
    if key_pressed == 'q':
        break

    slider.move(screen.play_field, key_pressed)
