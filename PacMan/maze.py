class Maze:
  _instance = None
  _initialized = False

  def __new__(cls):
      if cls._instance is None:
          cls._instance = super(Maze, cls).__new__(cls)
      return cls._instance

  def __init__(self):
      if not Maze._initialized:
          with open('pacman.txt', 'r') as f:
              self._grid = [list(line.strip()) for line in f.readlines()]
          Maze._initialized = True

  def __getitem__(self, row):
      return self._grid[row]

  def is_wall(self, r, c):
      return self._grid[r][c] == '*'

  def place_char(self, r, c, char):
      self._grid[r][c] = char

  def __str__(self):
      return '\n'.join(''.join(row) for row in self._grid)

  def search_maze(self, char):
      for r in range(len(self._grid)):
          for c in range(len(self._grid[r])):
              if self._grid[r][c] == char:
                  return [r, c]
      return [-1, -1]

  def count_dots(self):
      return sum(row.count('.') for row in self._grid)

