from random import randrange
from dragon import Dragon
import random

class FlyingDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._swoops = 5

    def special_attack(self, hero):
        if self._swoops > 0:
            damage = randrange(5, 8)
            hero.take_damage(damage)
            self._swoops -= 1
            print(f"\n~{damage}DMG\nThe flying dragon smacks into you by swooping in!\n")
        else:
            print(f"{self.get_name()} tried to swoop in, but it's tired.")
            print(f"{self.get_name()} resorts to normal attacks")
            self.basic_attack(hero)


    def __str__(self):
        return f"{super().__str__()}\n   Remaining Swoops Left: {self._swoops}"


