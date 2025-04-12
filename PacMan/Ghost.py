import random
from maze import Maze

class Ghost:
    def __init__(self):
        self._maze = Maze()
        self._previous = '.'

    def move(self):
        g_r, g_c = self._maze.search_maze('G')
        p_r, p_c = self._maze.search_maze('P')

        if -1 in [g_r, g_c, p_r, p_c]:
            return False

        # Determine preferred direction
        directions = []
        if p_r < g_r: directions.append('up')
        elif p_r > g_r: directions.append('down')
        if p_c < g_c: directions.append('left')
        elif p_c > g_c: directions.append('right')

        # Try moving (preferred first, then random)
        for _ in range(10):
            if directions:
                direction = directions.pop(0)
            else:
                direction = random.choice(['up', 'down', 'left', 'right'])

            new_r, new_c = g_r, g_c
            if direction == 'up': new_r -= 1
            elif direction == 'down': new_r += 1
            elif direction == 'left': new_c -= 1
            elif direction == 'right': new_c += 1

            if not self._maze.is_wall(new_r, new_c):
                if self._maze[new_r][new_c] == 'P':
                    return True

                self._maze.place_char(g_r, g_c, self._previous)
                self._previous = self._maze[new_r][new_c] if self._maze[new_r][new_c] != 'G' else self._previous
                self._maze.place_char(new_r, new_c, 'G')
                return False

        return False