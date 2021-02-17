from colorama.ansi import Back
import numpy as np
from time import sleep, time
from screen import Screen, display, flush_display
from slider import Slider
from blocks import GreenBlocks, RedBlocks, BlueBlocks, IndestructibleBlocks, PowerupBlocks
from ball import Ball
# from ball import Ball, SecondBall
from score import Score
from powerup import Powerup
from input import getInput
from input import input_to


# Creating instances of classes
screen = Screen(30, 79)
slider = Slider()

blue_blocks = BlueBlocks(1, 'blue')
green_blocks = GreenBlocks(2, 'green')
red_blocks = RedBlocks(3, 'red')
indestructible_blocks = IndestructibleBlocks(10, 'white')
powerup_blocks = PowerupBlocks(1, 'yellow')

ball = Ball()
second_ball = Ball()
# second_ball = SecondBall()
score = Score()
power_up = Powerup()
key_input = getInput()


# Initializations
slider.init_slider(screen.play_field)

indestructible_blocks.init_blocks(screen.play_field, 15, 2)
red_blocks.init_blocks(screen.play_field, 10, 5)
powerup_blocks.init_blocks(screen.play_field, 50, 11)
green_blocks.init_blocks(screen.play_field, 10, 7)
blue_blocks.init_blocks(screen.play_field, 10, 10)

ball.init_ball(screen.play_field)

display(screen.play_field)
ball.print(screen.play_field)


#  Global variables
isTrue1 = True
isTrue2 = False
# expand, shrink, miltiple, fast, through, grab, powerup
isPowerup = [False]*6
start_time = time()


def hold_ball():
    # Queue to start game
    print('Adjust the board and press P to resume')
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
    num = 1
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


def update_second_block_strength():
    num = 1
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
            isTrue2 = True
            second_ball.start = [ball.collided_with[0]
                                 [0]+1, ball.collided_with[0][1]+1]
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


def main():
    display(screen.play_field)

    all_blocks = combine_all_blocks()
    global isTrue1
    global isTrue2
    global isPowerup

    check_powerup()

    if isTrue1:
        isTrue1 = ball.set_state(screen.play_field, all_blocks, [
            slider.slider_width[0], slider.slider_width[1]])
        ball.print(screen.play_field)
    if isTrue2:
        isTrue2 = second_ball.set_state(screen.play_field, all_blocks, [
            slider.slider_width[0], slider.slider_width[1]])
        second_ball.print(screen.play_field)

    if ball.collided_with is not None:
        isPowerup = [0.5 > i for i in np.random.rand(7)]
        update_block_strength()
        score.update_score(len(ball.collided_with), int(time() -
                                                        start_time), 1, screen.play_field)
    refresh_all_blocks()

    if second_ball.collided_with is not None:
        update_second_block_strength()
        score.update_score(len(second_ball.collided_with), int(time() -
                                                               start_time), 1, screen.play_field)
    refresh_all_blocks()

    score.update_score(0, int(time()-start_time), 1, screen.play_field)
    if not (isTrue1 or isTrue2):
        score.update_score(0, int(time()-start_time), 0, screen.play_field)
        display(screen.play_field)

    return isTrue1 or isTrue2


hold_ball()

while main():
    key_pressed = input_to(key_input.__call__)
    if key_pressed == 'q':
        break
    slider.move(screen.play_field, key_pressed)
    pass
