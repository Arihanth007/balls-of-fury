# balls-of-fury
Game that run on your terminal coded in python. Some functionalities may not work on windows. Works best on linux and macOS.

## Game Objective
Break all blocks present on the screen to win the game.
A life is lost when the ball misses the paddle and hits the bottom of the screen. When all lives are lost the game ends

## Controls
On starting the game you can adjust the location of the paddle and press 'p'on your keyboard to release the ball.
Press 'a' to move the slider one step to the left and 'd' to move it one step to the right.
Press 'q' to quit the game at any moment.

## Game Components
### Paddle 
It is controlled by the user to send the ball in a specific direction. The farther from the centre of the paddle the ball collides, the faster it moves.
### Blocks 
There are 5 types of blocks. The blue blocks are worth one point, green are worth two, red are worth 3, white are indestructible and yellow are exploding in nature. Points are also the number of collision for the blocks to break. Hitting an exploding block destroys every block in a one brick vicinity.
### Ball
This moves around the screen and collides with obstacles.
### Wall
This is the container of the game.

## Power-Ups
There are six power-ups. These are randomly generated on hitting some blocks and are represented by magenta blocks. Expanding of the paddle, shrinking of the paddle, mutiple balls, sped up ball, pass-through-anything ball and paddle grab come into effect on taking the power-up.
