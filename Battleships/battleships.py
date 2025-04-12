'''
Author: Thomas Johnson
Date: 2/11/2025
Project: Program allows User to play battleship
'''
import random
def reset_game():
    grid = [[]]
    enemy_row = random.randint(0,4)
    enemy_col = random.randint(0,4)

def display_board():
    grid = [[' ', '  1', ' 2', ' 3', ' 4', ' 5'],
            ['A', ' ~', ' ~', ' ~', ' ~', ' ~'],
            ['B', ' ~', ' ~', ' ~', ' ~', ' ~'],
            ['C', ' ~', ' ~', ' ~', ' ~', ' ~'],
            ['D', ' ~', ' ~', ' ~', ' ~', ' ~'],
            ['E', ' ~', ' ~', ' ~', ' ~', ' ~']]
    row = ['A','B','C','D','E']
    for idx, row in enumerate(grid):
        print(row[idx], ' '.join(row))

def get_row():
    rows = ['A','B','C','D','E']
    cols = ['1','2','3','4','5']
    row = input("Predict the Enemies row", rows).upper()
    col = int(input("Predict the Enemis column", cols))
    return rows.index(row), int(col) - 1

def fire_shot(grid, solution, row, col):
    result = {"hit" : '*', "miss" : 'x'}
    if grid[row][col] != "~":
        print("This location is already selected")
        return False

    if row == enemy_row and col == enemy_col:
        grid[row][col] = '*'
        print("You hit the enemy ship!")
        return True
    else:
        grid[row][col] = 'x'
        print("You missed...")
        return False

def main_menu():
    count = 0
    while True:
        print("BattleShip Menu")
        print("1. Fire Shot")
        print("2. Show Solution")
        print("3. Quit")

        player = int(input("Press '1' to Fire!\n",))
        if player == 1:
            print("playing")
            display_board()
            row, col = get_row()
            if grid[row][col] != "~":
                print("This location is already selected")
            else:
                hit = fire_shot(grid, solution, row, col)
                if hit:
                    count += 1
                    while count == 4:
                        print("player wins!")
                        display_board()
                        reset_game()
        elif player == 2:
            print("Solutions:")
            display_board()
            reset_game()
        elif player == 3:
            print("...Quitting...")
            break
        else:
            print("Invalid Input! Use numbers 1-3")


main_menu()