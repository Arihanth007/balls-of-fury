import numpy as np
from config import height, width, black, powerups_array


class Powerup:

    def __init__(self) -> None:

        self.start = None  # starts as none
        self.__previous = None
        self.__current = None
        self.__array_of_powerups = powerups_array
        self.__temp = []
        for i in range(len(self.__array_of_powerups)):
            t = [False]*6
            t[i] = not(t[i])
            self.__temp.append(t)

    # tell it where to start from
    def init_powerup(self, x, y):

        self.start = [x, y]
        self.__previous = [self.start[0], self.start[1]]
        self.__current = [self.start[0]+1, self.start[1]]

    # powerup falls down from the block
    # checks if you have aqcuired it

    def simulate_powerup(self, play_field, slider_dimensions):

        # will enter only if a powerup exists
        if self.start is not None:
            if self.__current[0] < height-2:
                play_field[self.__current[0]][self.__current[1]] = 'powerup'
                play_field[self.__previous[0]
                           ][self.__previous[1]] = black
                # falls down by one
                self.__previous[0] += 1
                self.__current[0] += 1
            else:
                # collision with slider occurs
                play_field[self.__current[0]
                           ][self.__current[1]] = black
                play_field[self.__previous[0]
                           ][self.__previous[1]] = black
                self.start = None
                if self.__current[1] >= slider_dimensions[0] and self.__current[1] <= slider_dimensions[1]:
                    # randomly picks a powerup
                    return self.__temp[np.random.randint(1, 6)]

        return self.__array_of_powerups
