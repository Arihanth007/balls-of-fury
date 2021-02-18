from config import height, width, lives


class Score:

    def __init__(self) -> None:
        self.__score = 0
        self.__time = 0
        self.__lives = lives
        self.__output = 'Score: {}, Time: {}, Lives: {}'.format(
            self.__score, self.__time, self.__lives)

    # returns the status if the game
    # (game over or not)
    def update_score(self, count, tme, lives, play_field):

        # updates parameters during gameplay
        self.__score += count
        self.__time += tme
        self.__lives -= lives
        self.__output = 'Score: {}, Time: {}, Lives: {}'.format(
            self.__score, self.__time, self.__lives)

        # prints score, time and lives remaining
        for i in range(height):
            for j in range(width):
                if j < len(self.__output):
                    play_field[i][j] = self.__output[j]
                else:
                    break
            break

        return self.__lives >= 1
