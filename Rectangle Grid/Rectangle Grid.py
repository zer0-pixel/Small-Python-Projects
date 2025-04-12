'''
Author: Thomas Johnson, Linh Dong
Date 2/25/2025
Project:This program will allow the user to create a rectangle and move it around a grid.
'''

from Rectangle import Rectangle
import check_input
#Displays the grid and forms spaces into the rows
def display(grid):
    for row in grid:
        print(' '.join(row))
#Creates the 20 x 20 grid and recreates it everytime it is called
def reset(grid):
    return [["." for _ in range(20)] for _ in range(20)]
#Allows the user to create the grid
def place_rect(grid, rect):
    x, y = rect.get_coords()
    width, height = rect.get_dimensions()
    for i in range(y, y + height):
        for j in range(x, x + width):
            if 0 <= i < len(grid) and 0 <= j < len(grid[1]):
                grid[i][j] = '*'
#Gives the user a prompt to create the size of the rectangle and move it around.
def main():
    rect_width = check_input.get_int_range("Enter rectangle width (1-5): ", 1, 5)
    rect_height = check_input.get_int_range("Enter rectangle height (1-5): ", 1, 5)
    grid_size = 20
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    rect = Rectangle(rect_width, rect_height)
    place_rect(grid, rect)
    w, h = rect.get_dimensions()
    display(grid)
#Loops the direction prompt to the user, so the user can continue moving their piece around the grid
    while True:
        user = check_input.get_int_range("|Directions|\n1 - Move Up\n2 - Move Down\n3 - Move Left\n4 - Move Right\n5 - Stop\nInput: ", 1, 5)
#Checks the user input to move around or block the user because their piece hits the edge
        if user == 1:
            if rect.y == 0:
                print("***Cannot move beyond the grid.***")
            else:
                rect.move_up()
        elif user == 2:
            if rect.y + h == 20:
                print("***Cannot move beyond the grid.***")
            else:
                rect.move_down()
        elif user == 3:
            if rect.x == 0:
                print("***Cannot move beyond the grid.***")
            else:
                rect.move_left()
        elif user == 4:
            if rect.x + w == 20:
                print("***Cannot move beyond the grid.***")
            else:
                rect.move_right()
#Stops the program
        elif user == 5:
            break
#Calls the functions
        grid = reset(grid)
        place_rect(grid, rect)
        display(grid)

main()