'''
Author: Thomas Johnson, Linh Dong
Date: 3/6/2025
Project: Creates die class to make creating a die object easier
'''
import random

class Die:
    def __init__(self, sides = 6):
        self._sides = sides
        self._values = self.roll()

    def roll(self):
        self.value = random.randint(1, self._sides)
        return self.value

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __sub__(self, other):
        return self.value - other.value
