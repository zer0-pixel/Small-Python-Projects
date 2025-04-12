"""
Author: Thomas Johnson, Lihn Dong
Date: 4/8/2025
Program: User plays PACMAN. Collect the dots and avoid the ghost.
"""


from maze import Maze
from pacman import Pacman
from Ghost import Ghost

class Game:
# Initializes the objects set for the game
    def __init__(self):
        self._maze = Maze()
        self._player = Pacman()
        self._ghost = Ghost()

# Displays the maze to the player
    def _display(self):
        print("\nCurrent Maze:")
        print(self._maze)
        print(f"Dots remaining: {self._maze.count_dots()}")
        print("Controls: w=Up, a=Left, s=Down, d=Right, q=Quit")

# Display the instruction keys to the player
    def _get_move(self):
        while True:
            move = input("Your move: ").lower()
            if move in ['w', 'a', 's', 'd', 'q']:
                return move
            print("Invalid input! Use WASD or Q to quit")

# Main Game start
    def run(self):
        print("=== PAC-MAN GAME ===")
        print("Eat all dots while avoiding the ghost!")

        while True:
            self._display()
            move = self._get_move()

            if move == 'q':
                print("Game quit!")
                break

            # Player move
            player_caught = self._player.move(move)
            if player_caught:
                self._display()
                print("GAME OVER! Ghost caught you!")
                break

            if self._maze.count_dots() == 0:
                self._display()
                print("YOU WIN! All dots eaten!")
                break

            # Ghost move
            ghost_caught = self._ghost.move()
            if ghost_caught:
                self._display()
                print("GAME OVER! Ghost caught you!")
                break

if __name__ == "__main__":
    game = Game()
    game.run()