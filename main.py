from colorama.ansi import Back
import numpy as np
from playsound import playsound
from time import sleep, time
from screen import Screen, display, clear_entire_screen
from slider import Slider
from blocks import GreenBlocks, RedBlocks, BlueBlocks, IndestructibleBlocks, PowerupBlocks, RainbowBlocks
from ball import Ball
from score import Score
from powerup import Powerup
from input import getInput
from input import input_to
from config import height, width, powerups_array, black, block_drop_time, isSound


# Creating instances of classes
screen = Screen(height, width)
slider = Slider()

blue_blocks = BlueBlocks(1, 'blue')
green_blocks = GreenBlocks(2, 'green')
red_blocks = RedBlocks(3, 'red')
indestructible_blocks = IndestructibleBlocks(np.inf, 'white')
powerup_blocks = PowerupBlocks(1, 'yellow')
rainbow_blocks = RainbowBlocks()

ball = Ball()
second_ball = Ball()
score = Score()
power_up = Powerup()
key_input = getInput()


# Initializations
slider.init_slider(screen.play_field)

indestructible_blocks.init_blocks(screen.play_field, 6, 2)
red_blocks.init_blocks(screen.play_field, 12, 5)
powerup_blocks.init_blocks(screen.play_field, 50, 8)
green_blocks.init_blocks(screen.play_field, 12, 7)
blue_blocks.init_blocks(screen.play_field, 6, 10)
rainbow_blocks.init_blocks(screen.play_field, 12, 12)

ball.init_ball(screen.play_field)
display(screen.play_field)
ball.print(screen.play_field)


#  Global variables
isTrue1 = True
isTrue2 = False
isTrue3 = True
# expand, shrink, miltiple, fast, through, grab, canon, fireball
isPowerup = powerups_array
# isPowerup[-1] = True  # testing
start_time = time()
isPowerup_change_time = time()
level = 1
isLevelUp = True
output = ''
isDropblocks = True
isBossBullets = True


# Reduces life of primary ball by 1
def update_lives():

    # Creates a new instance of the ball
    global ball

    global output
    output = ''

    # Clears out the previous ball
    screen.play_field[ball.previous[0]][ball.previous[1]] = Back.BLACK + ' '
    screen.play_field[ball.current[0]][ball.current[1]] = Back.BLACK + ' '

    ball = Ball()

    # Initializes the new ball
    ball.init_ball(screen.play_field)
    ball.print(screen.play_field)

    # player can set starting point
    hold_ball()


# Player can set the starting release of the ball
# Press P to release
def hold_ball():

    print('Adjust the paddle using A, D and press P to release the ball')
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
    rainbow_blocks.refresh_blocks(screen.play_field)


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
            block[2] = 'blue'
            blue_blocks.blocks.append(block)
        elif color == 'red':
            red_blocks.reduce_block_strength(
                block, screen.play_field, num)
            block[2] = 'green'
            green_blocks.blocks.append(block)
        elif color == 'blue':
            blue_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'yellow':
            # collision with exploding block
            num = np.inf
            powerup_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'white':
            indestructible_blocks.reduce_block_strength(
                block, screen.play_field, num)
        try:
            rainbow_blocks.reduce_block_strength(
                block, screen.play_field, num)
        except:
            pass


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
            block[2] = 'blue'
            blue_blocks.blocks.append(block)
        elif color == 'red':
            red_blocks.reduce_block_strength(
                block, screen.play_field, num)
            block[2] = 'green'
            green_blocks.blocks.append(block)
        elif color == 'blue':
            blue_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'yellow':
            # collision with exploding block
            num = np.inf
            powerup_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'white':
            indestructible_blocks.reduce_block_strength(
                block, screen.play_field, num)
        try:
            rainbow_blocks.reduce_block_strength(
                block, screen.play_field, num)
        except:
            pass


# Called on collision of bullets
# Reduces block strength by 1
def update_block_strength_bullet():

    num = 1  # by default

    for block in slider.collided_with:
        color = block[2]
        if color == 'green':
            green_blocks.reduce_block_strength(
                block, screen.play_field, num)
            block[2] = 'blue'
            blue_blocks.blocks.append(block)
        elif color == 'red':
            red_blocks.reduce_block_strength(
                block, screen.play_field, num)
            block[2] = 'green'
            green_blocks.blocks.append(block)
        elif color == 'blue':
            blue_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'yellow':
            # collision with exploding block
            num = np.inf
            powerup_blocks.reduce_block_strength(
                block, screen.play_field, num)
        elif color == 'white':
            indestructible_blocks.reduce_block_strength(
                block, screen.play_field, num)
        try:
            rainbow_blocks.reduce_block_strength(
                block, screen.play_field, num)
        except:
            pass


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
    for block in rainbow_blocks.blocks:
        all_blocks.append(block)

    return all_blocks


# all blocks are moved
# down by 1 unit
def move_blocks():
    green_blocks.push_down(screen.play_field)
    red_blocks.push_down(screen.play_field)
    blue_blocks.push_down(screen.play_field)
    indestructible_blocks.push_down(screen.play_field)
    powerup_blocks.push_down(screen.play_field)
    rainbow_blocks.push_down(screen.play_field)


# clears contents of all blocks
def clear_all_blocks():
    green_blocks.clear_all(screen.play_field)
    red_blocks.clear_all(screen.play_field)
    blue_blocks.clear_all(screen.play_field)
    indestructible_blocks.clear_all(screen.play_field)
    powerup_blocks.clear_all(screen.play_field)
    rainbow_blocks.clear_all(screen.play_field)


# Goes through the powerup array
# calls the respective powerup
# resets the powerup array
def check_powerup():

    global isTrue2, isPowerup, output, isPowerup_change_time

    if isPowerup[0]:
        output = 'Expand paddle'
        slider.expand_slider(screen.play_field)
        isPowerup[0] = False

    if isPowerup[1]:
        output = 'Shrink Paddle'
        slider.shrink_slider(screen.play_field)
        isPowerup[1] = False

    if isPowerup[2]:
        if isTrue1:
            # sets up ball 2 requirements
            output = '2 Balls'
            isTrue2 = True
            second_ball.start = [height-3, int(width/2)]
        isPowerup[2] = False

    if isPowerup[3]:
        output = 'Fast Ball'
        ball.increase_speed()
        second_ball.increase_speed()
        isPowerup[3] = False

    if isPowerup[4]:
        output = 'Through Ball'
        ball.pass_through_blocks()
        second_ball.pass_through_blocks()
        isPowerup[4] = False

    if isPowerup[5]:
        output = 'Hold Ball'
        hold_ball()
        isPowerup[5] = False

    if isPowerup[6]:
        output = 'Canon'
        isPowerup[6] = False

    if isPowerup[7]:
        output = 'Fire Ball'
        ball.fire_ball()
        second_ball.fire_ball()
        isPowerup[7] = False

    # canon powerup is active
    if output == 'canon':

        # prints canons on either side
        # of the slider
        slider.print_canons(screen.play_field)

        # sends new bullet coordinates
        # updates old bullet coordinates
        slider.shoot_bullets(
            slider.slider_width[0], slider.slider_width[1], screen.play_field, combine_all_blocks())
    else:
        # updates old bullet coordinates
        slider.shoot_bullets(None, None, screen.play_field,
                             combine_all_blocks())

    # displayes the powerup and timer
    if output == 'canon' or output == 'Through Ball' or output == 'Fast Ball' or output == 'Shrink Paddle' or output == 'Expand paddle' or output == 'Fire Ball':
        print('Powerup: '+output, 5-int(time()-isPowerup_change_time))


# Levels up the game
def level_up():

    global isLevelUp, slider, ball, isPowerup, output

    # levels up
    if isLevelUp:

        # initializes new slider
        slider = Slider()
        slider.init_slider(screen.play_field)

        # sets old ball position to black
        # and initializes new ball
        screen.play_field[ball.current[0]][ball.current[1]] = black
        ball = Ball()
        ball.init_ball(screen.play_field)
        ball.print(screen.play_field)

        # powerups are reset
        isPowerup = powerups_array
        isLevelUp = False
        output = ''

        # block patterns are initialized
        if level == 2:
            indestructible_blocks.init_blocks(screen.play_field, 8, 2)
            red_blocks.init_blocks(screen.play_field, 16, 5)
            powerup_blocks.init_blocks(screen.play_field, 50, 8)
            green_blocks.init_blocks(screen.play_field, 16, 7)
            blue_blocks.init_blocks(screen.play_field, 10, 10)
            rainbow_blocks.init_blocks(screen.play_field, 12, 12)
        elif level == 3:
            indestructible_blocks.init_blocks(screen.play_field, 12, 5)
            blue_blocks.init_blocks(screen.play_field, 50, 7)
            rainbow_blocks.init_blocks(screen.play_field, 8, 10)

        # starts level by
        # holding the ball
        hold_ball()


# Main function that runs the code
def main():

    global isDropblocks, isBossBullets

    # handles moving down of blocks
    # every block_drop_time number of seconds
    if int(time()-start_time) % block_drop_time == 0 and int(time()-start_time) != 0:
        if isDropblocks:
            move_blocks()
            isDropblocks = False
    elif int(time()-start_time) % (block_drop_time+1) == 0:
        isDropblocks = True

    # causes blocks to change color
    rainbow_blocks.rainbow_effect()

    # Prints the entire screen
    display(screen.play_field)

    # Initialize some variables
    all_blocks = combine_all_blocks()

    global isTrue1, isTrue2, isTrue3, isPowerup, isPowerup_change_time, level, isLevelUp, output
    slider_dimensions = [slider.slider_width[0], slider.slider_width[1]]

    # game ends if no blocks or left till level 2
    # or if boss is defeated in level 3
    if all_blocks.count == 0 or (level == 3 and slider.boss_lives == 0):
        level += 1
        isLevelUp = True

    # game ends if blocks
    # drop to slider height
    for block in all_blocks:
        if block[0] >= height-3:
            isTrue3 = False

    # saving some values
    # since they get updated
    ball_x, ball_y = ball.xv, ball.yv
    sball_x, sball_y = second_ball.xv, second_ball.yv

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
        if 0.4 > np.random.rand() and power_up.start is None:
            # powerups are available
            power_up.init_powerup(
                ball.collided_with[0][0], ball.collided_with[0][1], ball_x, ball_y)
        # Update block strength and score
        update_block_strength()
        score.update_score(len(ball.collided_with), int(time() -
                                                        start_time), 0, level, screen.play_field)

    # Checks for Ball 2 collision with blocks
    if second_ball.collided_with is not None:
        if 0.4 > np.random.rand() and power_up.start is None:
            # powerups are available
            power_up.init_powerup(
                second_ball.collided_with[0][0], second_ball.collided_with[0][1], sball_x, sball_y)
        # Update block strength and score
        update_second_block_strength()
        score.update_score(len(second_ball.collided_with), int(time() -
                                                               start_time), 0, level, screen.play_field)

    # updates score
    score.update_score(len(slider.collided_with), int(
        time()-start_time), 0, level, screen.play_field)

    # updates boss lives
    if ball.boss_collision:
        slider.boss_lives -= 1
    if second_ball.boss_collision:
        slider.boss_lives -= 1

    # removes blocks that have been
    # shot with canon (powerup)
    if slider.collided_with.count != 0:
        update_block_strength_bullet()

    # set the powerups randomly
    # if above conditions are met
    isPowerup, temp = power_up.simulate_powerup(
        screen.play_field, slider_dimensions)
    if temp is not None:
        isPowerup_change_time = temp
    # powerups last for 5 seconds
    if time()-isPowerup_change_time >= 5:
        ball.reset(screen.play_field)
        second_ball.reset(screen.play_field)
        slider.reset(screen.play_field)
        isPowerup = powerups_array
        output = ''
    check_powerup()
    refresh_all_blocks()

    # updates score and lives
    score.update_score(0, int(time()-start_time), 0, level, screen.play_field)
    if not (isTrue1 or isTrue2):
        if score.update_score(
                0, int(time()-start_time), 1, level, screen.play_field):
            isTrue1 = True
            update_lives()
        display(screen.play_field)

    # Boss is introduced in level 3
    if level == 3:

        # prints boss details
        print('Boss Lives = ', slider.boss_lives)
        slider.isBoss = True

        # boss drops bombs every 3 seconds
        if int(time()-start_time) % 3 == 0 and int(time()-start_time) != 0:
            if isBossBullets:
                # new bomb
                # updates old bomb
                if slider.boss_shoots_bullets(screen.play_field, True):
                    # reduces 1 life of slider
                    isTrue3 = score.update_score(
                        0, int(time()-start_time), 1, level, screen.play_field)
                    update_lives()
                isBossBullets = False
        elif int(time()-start_time) % (3+1) == 0:
            isBossBullets = True

        # updates old bomb
        if slider.boss_shoots_bullets(screen.play_field, False):
            # reduces life by 1
            isTrue3 = score.update_score(
                0, int(time()-start_time), 1, level, screen.play_field)
            update_lives()

    # continues if either ball is active
    # and blocks haven't reached the slider
    return (isTrue1 or isTrue2) and isTrue3


# code starts executing from here
# starts from hold position
hold_ball()

# Press q to quit game
while level <= 3 and main():

    # checks for level ups
    if level != 1 and isLevelUp:
        clear_entire_screen(screen.play_field)
        level_up()

    key_pressed = input_to(key_input.__call__)

    # quits game
    if key_pressed == 'q':
        break
    # levels up
    elif key_pressed == 'n':
        clear_all_blocks()
        clear_entire_screen(screen.play_field)
        level += 1
        isLevelUp = True

    # moves slider
    slider.move(screen.play_field, key_pressed)

# sound effect
if isSound:
    playsound('sounds/gameover.wav')
