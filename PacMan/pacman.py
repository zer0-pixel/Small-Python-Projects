from maze import Maze

class Pacman:
    def __init__(self):
        self._maze = Maze()

    def move(self, direction):
        r, c = self._maze.search_maze('P')
        if r == -1:
            return False

        new_r, new_c = r, c
        if direction == 'w': new_r -= 1
        elif direction == 'a': new_c -= 1
        elif direction == 's': new_r += 1
        elif direction == 'd': new_c += 1

        if self._maze.is_wall(new_r, new_c):
            return False

        if self._maze[new_r][new_c] == 'G':
            return True

        self._maze.place_char(r, c, ' ')
        self._maze.place_char(new_r, new_c, 'P')
        return False