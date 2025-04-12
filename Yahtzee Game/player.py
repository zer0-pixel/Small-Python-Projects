'''
Author: Thomas Johnson, Linh Dong
Date: 3/6/2025
Project: create player class to make creating a player object easier
'''
import die

class Player:
    def __init__(self):
        self._dice = [die.Die(), die.Die(), die.Die()]
        self._player_points = 0
        #Creates players points
    def points(self):
        return self._player_points

    def roll_dice(self):
        for d in self._dice:
            d.roll()

    # Checks for 3 of a kind in dice roll
    def has_three_of_a_kind(self):
        values = [d.value for d in self._dice]
        if values[0] == values[1] == values[2]:
            self._player_points += 3
            return True
        return False

    #Checks for pairs in dice roll
    def has_pair(self):
        values = [d.value for d in self._dice]
        if (values[0] == values[1]) or (values[1] == values[2]) or (values[0] == values[2]):
            self._player_points += 1
            return True
        return False

    #Checks for series in dice roll
    def has_series(self):
        if self._dice[1] - self._dice[0] == 1 and self._dice[2] - self._dice[1] == 1:
            self._player_points += 2
            return True
        return False

    #Creates the dice display
    def __str__(self):
        return f"D1={self._dice[0]}, D2={self._dice[1]}, D3={self._dice[2]}"
