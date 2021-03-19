from colorama import Back

'''All number values must be integers'''

# Screen dimensions
height = 30
width = 79

# Colors
red = Back.RED + ' '
blue = Back.BLUE + ' '
green = Back.GREEN + ' '
black = Back.BLACK + ' '
yellow = Back.YELLOW + ' '
magenta = Back.MAGENTA + ' '
white = Back.WHITE + ' '

# Slider dimensions
Slider_Width = int(8/2)
Expanded_Width = int(16/2)
Shrunk_width = int(4/2)

# expand, shrink, miltiple, fast, through, grab, canon, fireball
powerups_array = [False]*8

# Number of lives
lives = 5

# time taken to drop blocks
block_drop_time = 10

isSound = True
