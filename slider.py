import numpy as np
from time import time, sleep
from screen import display
from config import height, width, black, Slider_Width, Shrunk_width, Expanded_Width


class Slider:

    def __init__(self):
        self.__swidth = 2*Slider_Width  # defines the slider width
        self.bullets = []
        self.collided_with = []
        self.boss_bullets = []
        self.boss_height = 3
        self.isBoss = False
        self.boss_lives = 3

    # initializes the slider on the screen
    def init_slider(self, play_field):
        self.slider_width = np.array(
            [int(width/2)-self.__swidth, int(width/2)+self.__swidth], dtype=int)
        self.slider_height = height-2

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

        if self.isBoss and self.boss_lives:
            mid = int((self.slider_width[0]+self.slider_width[1])/2)
            play_field[self.boss_height][mid-Shrunk_width] = '('
            play_field[self.boss_height][mid+Shrunk_width] = ')'
            for i in range(mid-Shrunk_width+1, mid+Shrunk_width):
                play_field[self.boss_height][i] = '-'

    # updates the slider on the screen
    def __print_slider(self, val, play_field):
        for i in range(1, width-1):
            play_field[self.slider_height][i] = black
        for i in range(1, width-1):
            if play_field[self.slider_height-1][i] == '|':
                play_field[self.slider_height-1][i] = black

        for i in range(1, width-1):
            if play_field[self.boss_height][i] == '(' or play_field[self.boss_height][i] == ')' or play_field[self.boss_height][i] == '-':
                play_field[self.boss_height][i] = black

        if val > 0 and self.slider_width[1]+val < width:
            self.slider_width[0] += val
            self.slider_width[1] += val
        if val < 0 and self.slider_width[0]+val > 0:
            self.slider_width[0] += val
            self.slider_width[1] += val

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

        if self.isBoss and self.boss_lives:
            mid = int((self.slider_width[0]+self.slider_width[1])/2)
            play_field[self.boss_height][mid-Shrunk_width] = '('
            play_field[self.boss_height][mid+Shrunk_width] = ')'
            for i in range(mid-Shrunk_width+1, mid+Shrunk_width):
                play_field[self.boss_height][i] = '-'

        display(play_field)

    # Press a to move left
    # Press d to move right
    def move(self, play_field, key_press):
        if key_press == 'd':
            self.__print_slider(2, play_field)
        elif key_press == 'a':
            self.__print_slider(-2, play_field)

    # shrinks the slider in half
    def shrink_slider(self, play_field):
        self.__swidth = 2*Shrunk_width
        self.slider_width[0] += Slider_Width
        self.slider_width[1] -= Slider_Width
        self.__print_slider(0, play_field)

    # expands the slider to double
    def expand_slider(self,  play_field):
        self.__swidth = 2*Expanded_Width
        # if self.slider_width[0] - Slider_Width <= 1:
        #     self.slider_width += (self.slider_width[0]-Slider_Width)
        # if self.slider_width[1] + Slider_Width >= width-1:
        #     self.slider_width += (self.slider_width[1]+Slider_Width)
        if self.slider_width[0] - Slider_Width <= 1:
            self.slider_width += abs(self.slider_width[0]-Slider_Width)
        if self.slider_width[1] + Slider_Width >= width-1:
            self.slider_width -= abs(self.slider_width[1]-Slider_Width)

        self.slider_width[0] -= Slider_Width
        self.slider_width[1] += Slider_Width
        self.__print_slider(0, play_field)

    def reset(self, play_field):
        if self.__swidth == 2*Slider_Width:
            return

        if self.slider_width[1]-self.slider_width[0] > 2*Slider_Width:
            self.slider_width[0] += Slider_Width
            self.slider_width[1] -= Slider_Width
        else:
            if self.slider_width[0] - Slider_Width <= 1:
                self.slider_width += abs(self.slider_width[0]-Slider_Width)
            if self.slider_width[1] + Slider_Width >= width-1:
                self.slider_width -= abs(self.slider_width[1]-Slider_Width)
            self.slider_width[0] -= Slider_Width
            self.slider_width[1] += Slider_Width

        self.__swidth = 2*Slider_Width
        self.__print_slider(0, play_field)

    def print_canons(self, play_field):
        play_field[self.slider_height-1][self.slider_width[0]] = '|'
        play_field[self.slider_height-1][self.slider_width[1]] = '|'

    def shoot_bullets(self, l, r, play_field, blocks):
        self.collided_with.clear()

        for bullet in self.bullets:
            play_field[bullet[0]][bullet[1]] = black

        if l is not None and r is not None:
            self.bullets.append([self.slider_height, l])
            self.bullets.append([self.slider_height, r])

        for indx, bullet in enumerate(self.bullets):
            if bullet[0] <= 1:
                self.bullets.remove(bullet)
            else:
                self.bullets[indx][0] -= 1

        for indx, bullet in enumerate(self.bullets):
            for block in blocks:
                if bullet[0] == block[0] and bullet[1] == block[1]:
                    self.collided_with.append(block)
                    self.bullets.remove(bullet)

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

        for bullet in self.bullets:
            play_field[bullet[0]][bullet[1]] = '.'

    def boss_shoots_bullets(self, play_field, isShoot):
        isCollided = False

        if self.boss_lives:
            for bullet in self.boss_bullets:
                play_field[bullet[0]][bullet[1]] = black

            if isShoot:
                y = int((self.slider_width[0]+self.slider_width[1])/2)
                self.boss_bullets.append([self.boss_height, y])

            for indx, bullet in enumerate(self.boss_bullets):
                if bullet[0] >= height-1:
                    self.boss_bullets.remove(bullet)
                else:
                    self.boss_bullets[indx][0] += 1

            for indx, bullet in enumerate(self.boss_bullets):
                if bullet[0] == height-2 and play_field[bullet[0]][bullet[1]] == '-':
                    isCollided = True

            for bullet in self.boss_bullets:
                print(bullet[0], bullet[1])
                play_field[bullet[0]][bullet[1]] = 'o'

        return isCollided
        # return (not isCollided)
