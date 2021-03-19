from time import sleep
import numpy as np
from playsound import playsound
from config import height, width, black, isSound


class Ball:

    def __init__(self):
        self.start = [height-3, int(width/2)]
        self.previous = [self.start[0]+1, self.start[1]+1]
        self.current = [self.start[0], self.start[1]]
        self.__next = [self.start[0], self.start[1]]
        self.x_velocity = 1
        self.y_velocity = 1
        self.collided_with = None
        self.power_up_collision = False
        self.xv = 1
        self.yv = 0
        self.boss_collision = False

    # sets the starting position
    def init_ball(self, play_field):
        play_field[self.start[0]][self.start[1]] = 'ball'

    # updates the ball location
    def print(self, play_field):
        play_field[self.previous[0]][self.previous[1]] = black
        play_field[self.current[0]][self.current[1]] = 'ball'

    # sets ball location to middle of slider
    def place_ball(self, play_field, slider_dimensions):

        # slider coordinates
        slider_width = slider_dimensions[1] - slider_dimensions[0]
        slider_mid = int(slider_dimensions[1] - (slider_width/2))

        t = slider_mid-self.current[1]
        if t != 0:
            play_field[self.current[0]][self.current[1]] = black
            self.current[1] += t
            self.__next[1] += t
            self.previous[1] += t
            play_field[self.current[0]][self.current[1]] = 'ball'
            self.start[1] = self.current[1]

    # powerup
    def increase_speed(self):
        self.x_velocity = 2
        self.y_velocity = 2

    # powerup
    def pass_through_blocks(self):
        self.power_up_collision = True

    def reset(self, play_field):
        play_field[self.previous[0]][self.previous[1]] = black
        self.x_velocity = 1
        self.y_velocity = 1
        self.power_up_collision = False

    # handles collision with slider
    def __check_slider_collision(self, x, y, play_field, slider_dimensions):

        # slider coordinates
        slider_width = slider_dimensions[1] - slider_dimensions[0]
        slider_mid = int(slider_dimensions[1] - (slider_width/2))

        # checks if ball has passed the slider
        if self.current[0] >= height-1-x:

            # checks if slider is in the bounds of the slider
            if self.current[1]+y >= slider_dimensions[0] and self.current[1]+y <= slider_dimensions[1]:

                # sets velocity according to how close
                # to the middle the collision took place
                self.y_velocity = 1 + np.abs(
                    slider_mid-(self.current[1]+y)) % 3

                # decides whether to reverse the y-direction
                if self.current[1]+y > slider_mid:
                    y = self.y_velocity
                else:
                    y = -self.y_velocity

                self.__next[0] -= x  # reverses x-direction
                self.__next[1] += y

                # returns true as collision with slider occurs
                return True
            else:
                if isSound:
                    playsound('sounds/lose.wav')
                # returns false as collision with slider was missed
                return False
        else:
            # return true as collision with slider might occur
            # since it hasn't reached the height of the slider
            return True

    # handles wall collisions
    def __check_wall_collision(self, x, y):

        # top and bottom collisions
        if self.current[0] + x > 1 and self.current[0] + x < height-1:
            self.__next[0] += x
        else:
            if isSound:
                playsound('sounds/wall_collision.wav')
            self.__next[0] -= x

        # left and right collisions
        if self.current[1] + y > 1 and self.current[1] + y < width-1:
            self.__next[1] += y
        else:
            if isSound:
                playsound('sounds/wall_collision.wav')
            self.__next[1] -= y

    # handles block collisions by
    # checking if a block is present
    # in the trajectory of the ball
    def __check_obstacle_collision(self, x, y, play_field, blocks):

        # x, y direction collision parameters
        # used in determining direction of refection
        # and collision
        X_collision = False
        Y_collision = False
        self.boss_collision = False

        # takes into account all the cells
        # that come in the balls trajectory
        collision_box = []
        for i in range(min(self.__next[0], self.__next[0]+x), max(self.__next[0], self.__next[0]+x)+1):
            for j in range(min(self.__next[1], self.__next[1]+y), max(self.__next[1], self.__next[1]+y)+1):
                collision_box.append([i, j])

        # check collision with every block
        for block in blocks:

            # checks for collision
            if [block[0], block[1]] in collision_box:
                if isSound:
                    playsound('sounds/random.wav')

                X_collision = True
                Y_collision = True

                # checks for horizontal collisions
                if self.__next[0] == block[0]:
                    X_collision = False
                # checks for vertical collisions
                if self.__next[1] == block[1]:
                    Y_collision = False

                self.collided_with = [block]  # sets collided block

                # checks if collided with exploding block
                if block[2] == 'yellow':

                    # stores all exploding blocks
                    for bl in blocks:
                        if bl[2] == 'yellow' and bl != block:
                            self.collided_with.append(bl)

                    # since these blocks destroy everything around it
                    # it stores all the blocks around it too
                    for bl in blocks:
                        if bl[2] != 'yellow':
                            for powerup_block in self.collided_with:
                                if (bl[0] == powerup_block[0]+1 or bl[0] == powerup_block[0]-1) and (bl[1] == powerup_block[1]+1 or bl[1] == powerup_block[1]-1):
                                    self.collided_with.append(bl)

        if not X_collision and not Y_collision:
            for ele in collision_box:
                if ele[1] >= width:
                    continue

                if play_field[ele[0]][ele[1]] == '(' or play_field[ele[0]][ele[1]] == ')' or (play_field[ele[0]][ele[1]] == '-' and ele[0] < height/2):

                    self.boss_collision = True
                    X_collision = True
                    Y_collision = True

                    # checks for horizontal collisions
                    if self.__next[0] == ele[0]:
                        X_collision = False
                    # checks for vertical collisions
                    if self.__next[1] == ele[1]:
                        Y_collision = False

                    break

        # no reflection for pass-through ball
        if (X_collision or Y_collision) and self.power_up_collision:
            self.__next[0] += x
            self.__next[1] += y
            return True

        # handles reflection directions
        if X_collision and Y_collision:
            self.__next[0] -= x
            self.__next[1] -= y
        elif X_collision:
            self.__next[0] -= x
            self.__next[1] += y
        elif Y_collision:
            self.__next[0] += x
            self.__next[1] -= y
        else:
            # no collision took place
            return False

        # collision took place
        return True

    def set_state(self, play_field, blocks, slider_dimensions):

        # makes a copy since these values
        # are changed by different functions
        x = self.x_velocity
        y = self.y_velocity

        # sets directionality
        if self.current[0] - self.previous[0] < 0:
            x *= -1
        if self.current[1] - self.previous[1] < 0:
            y *= -1

        self.xv = x
        self.yv = y

        # printing cause why not xD
        # print(x, y)

        # checks for slider collision
        # checks for obstacle collision
        # checks for wall collision
        if self.__check_slider_collision(x, y, play_field, slider_dimensions):

            if not self.__check_obstacle_collision(x, y, play_field, blocks):
                self.__check_wall_collision(x, y)
                self.collided_with = None

            # updates ball location
            play_field[self.previous[0]
                       ][self.previous[1]] = black
            self.previous = [self.current[0], self.current[1]]
            self.current = [self.__next[0], self.__next[1]]

            # ball lives on
            return True

        # ball has dies
        return False
