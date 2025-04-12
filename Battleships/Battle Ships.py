'''
Author: Thomas Johnson, Linh Dong
Date: 2/11/2025
Project: Program allows User to play battleship
'''

import random

#Creates the game and also resets it when player presses 1 in the menu
def reset_game():
    grid = [["~" for _ in range(5)]for _ in range(5)]
    enemy_row = random.randint(0,3)
    enemy_col = random.randint(0,3)
    enemy = [(enemy_row, enemy_col),
             (enemy_row, enemy_col + 1),
             (enemy_row + 1, enemy_col),
             (enemy_row + 1, enemy_col + 1)]

    return grid, enemy

#The board gets programmed and displayed to the user
def display_board(grid):
    print('  1 2 3 4 5')
    rows = ['A','B','C','D','E']
    for idx, row in enumerate(grid):
        print(rows[idx], ' '.join(row))


#Gets users input to fire a shot at a row and column
def get_row():
    rows = ['A','B','C','D','E']
    cols = ['1','2','3','4','5']

    row = input("Predict the Enemies row\n").upper()
    if row in rows:
        row_idx = rows.index(row)
    else:
        print("Invalid Input")
        return get_row()

    col = input("Predict the Enemies column\n")
    if col in cols:
        col_idx = int(col) - 1
    else:
        print("Invalid Input")
        return get_row()

    return row_idx, col_idx

#Gets results from user and computer to determine if the user hit or miss the computer
def fire_shot(grid, enemy, row = None, col = None, solution = False):
    if solution:
        for row, col in enemy:
            grid[row][col] = '*'
        display_board(grid)
        return

    if not (0 <= row < 5 and 0 <= col < 5):
        print("Invalid Location")
        return False

    if grid[row][col] != "~":
        print("This location is already selected")
        if grid[row][col] != "~" == 4:
            print("You've Been Hit!\n"
                  "You Lose")
            main_menu()
        return False

    if (row, col) in enemy:
        grid[row][col] = '*'
        print("You hit the enemy ship!")
        display_board(grid)
        return True
    else:
        grid[row][col] = 'x'
        print("You missed...")
        display_board(grid)
        return False

#This is the function that prints the menu to the player
def main_menu():
    grid, enemy = reset_game()
    hits = 0
    while True:
        print("BattleShips | Menu")
        print("1. Fire Shot")
        print("2. Show Solution")
        print("3. Quit")

        try:
            player = int(input("Press '1' to Fire!\n"))
        except:
            print("Invalid numbers! Choose numbers 1 - 3")
            continue
#Player gets prompted to play game, show solution to the board, or quit the game
        if player == 1:
            print("playing")
            display_board(grid)
            row, col = get_row()
            if fire_shot(grid, enemy, row, col):
                hits += 1
                if hits == 4:
                    print("\nPlayer wins | You've Destroyed the Enemy Ship\n")
                    grid, solution = reset_game()
        elif player == 2:
            print("Solution:")
            fire_shot(grid, enemy, solution = True)
            grid, enemy = reset_game()
        elif player == 3:
            print("...Quitting...")
            break
        else:
            print("Invalid Input! Use numbers 1-3")



main_menu()