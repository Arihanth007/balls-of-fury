import numpy as np
from playsound import playsound
from time import time
from config import height, width, black, powerups_array, isSound


class Powerup:

    def __init__(self) -> None:

        self.start = None  # starts as none
        self.__previous = None
        self.__current = None
        self.__next = None
        self.__array_of_powerups = powerups_array
        self.__temp = []
        self.x_vel = 1
        self.y_vel = 0
        self.__count = 3
        for i in range(len(self.__array_of_powerups)):
            t = [False]*len(self.__array_of_powerups)
            t[i] = not(t[i])
            self.__temp.append(t)

    # tell it where to start from
    def init_powerup(self, x, y, xvel, yvel):

        self.start = [x, y]
        self.x_vel = xvel
        self.y_vel = yvel
        self.__previous = [self.start[0], self.start[1]]
        self.__current = [self.start[0]+self.x_vel, self.start[1]+self.y_vel]
        self.__next = [self.start[0]+self.x_vel, self.start[1]+self.y_vel]
        self.__count = 3

    def simulate_powerup(self, play_field, slider_dimensions):

        self.__count -= 1
        # will enter only if a powerup exists
        if self.start is not None:
            if self.__current[0] < height-2:
                play_field[self.__current[0]][self.__current[1]] = 'powerup'
                play_field[self.__previous[0]
                           ][self.__previous[1]] = black

                if self.__current[0] + self.x_vel < 1:
                    self.x_vel *= -1
                if self.__count <= 0:
                    self.x_vel = abs(self.x_vel)
                if self.__current[1] + self.y_vel < 1 or self.__current[1] + self.y_vel > width-1:
                    self.y_vel *= -1

                self.__next[0] += self.x_vel
                self.__next[1] += self.y_vel

                self.__previous = [self.__current[0], self.__current[1]]
                self.__current = [self.__next[0], self.__next[1]]

            else:
                # collision with slider occurs
                play_field[self.__current[0]
                           ][self.__current[1]] = black
                play_field[self.__previous[0]
                           ][self.__previous[1]] = black

                self.start = None
                if self.__current[1] >= slider_dimensions[0] and self.__current[1] <= slider_dimensions[1]:
                    if isSound:
                        playsound('sounds/powerup.wav')
                    # randomly picks a powerup
                    return self.__temp[np.random.randint(0, len(powerups_array))], time()

        return self.__array_of_powerups, None
