import numpy as np
from time import time, sleep
from screen import display
from config import height, width, black, Slider_Width, yellow


class Boss:

    def __init__(self):
        self.__width = 2  # defines the boss width
        self.bullets = []
        self.boss_height = 3

    # initializes boss on the screen
    def init_boss(self, play_field, mid):

        self.boss_width = [mid, mid+1]

        # play_field[self.boss_height][int(self.boss_width[0])] = '('
        # play_field[self.boss_height][int(self.boss_width[1])] = ')'

    # updates the boss on the screen
    def print_boss(self, play_field, mid):
        for i in range(1, width-1):
            if play_field[self.boss_height][i] == '(' or play_field[self.boss_height][i] == ')':
                play_field[self.boss_height][i] = black

        self.boss_width = [mid, mid+1]

        # play_field[self.boss_height][int(self.boss_width[0])] = '('
        # play_field[self.boss_height][int(self.boss_width[1])] = ')'

        # display(play_field)
        pass

    def shoot_bullets(self, y, play_field, isShoot):
        isCollided = False

        for bullet in self.bullets:
            play_field[bullet[0]][bullet[1]] = black

        if isShoot:
            self.bullets.append([self.boss_height, int(y)])

        for indx, bullet in enumerate(self.bullets):
            if bullet[0] >= height-1:
                self.bullets.remove(bullet)
            else:
                self.bullets[indx][0] += 1

        for indx, bullet in enumerate(self.bullets):
            if bullet[0] == height-2 and play_field[bullet[0]][bullet[1]] == '-':
                isCollided = True

        for bullet in self.bullets:
            print(bullet[0], bullet[1])
            sleep(1)
            # play_field[bullet[0]][bullet[1]] = 'o'

        return (not isCollided)
