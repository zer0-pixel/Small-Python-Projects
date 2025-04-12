from random import randrange
from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._fire_shots = 3

    def special_attack(self, hero):
        if self._fire_shots > 0:
            damage = randrange(6, 9)
            hero.take_damage(damage)
            self._fire_shots -= 1
            print(f"\n~{damage}DMG\nYou've been hit by a fireball!\n")
        else:
            print(f"{self.get_name()} tried to shoot a fireball...but couldn't")
            print(f"{self.get_name()} resorts to normal attacks")
            self.basic_attack(hero)


    def __str__(self):
        return f"{super().__str__()}\n   Fire Shots Remaining: {self._fire_shots}"

