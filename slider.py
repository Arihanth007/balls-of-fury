import numpy as np
from screen import display
from config import height, width, black, Slider_Width, Shrunk_width, Expanded_Width


class Slider:

    def __init__(self):
        self.__swidth = 2*Slider_Width  # defines the slider width

    # initializes the slider on the screen
    def init_slider(self, play_field):
        self.slider_width = np.array(
            [int(width/2)-self.__swidth, int(width/2)+self.__swidth], dtype=int)
        self.slider_height = height-2

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

    # updates the slider on the screen
    def __print_slider(self, val, play_field):
        for i in range(1, width-1):
            play_field[self.slider_height][i] = black

        if val > 0 and self.slider_width[1]+val < width:
            self.slider_width[0] += val
            self.slider_width[1] += val
        if val < 0 and self.slider_width[0]+val > 0:
            self.slider_width[0] += val
            self.slider_width[1] += val

        for i in range(self.slider_width[0], self.slider_width[1]):
            play_field[self.slider_height][i] = '-'

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
        self.init_slider(play_field)

    # expands the slider to double
    def expand_slider(self,  play_field):
        self.__swidth = 2*Expanded_Width
        if self.slider_width[0] - Slider_Width <= 1:
            self.slider_width += (self.slider_width[0]-Slider_Width)
        if self.slider_width[1] + Slider_Width >= width-1:
            self.slider_width += (self.slider_width[1]+Slider_Width)
        self.slider_width[0] -= Slider_Width
        self.slider_width[1] += Slider_Width
        self.init_slider(play_field)
