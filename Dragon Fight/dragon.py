import random
from random import randrange
from entity import Entity


class Dragon(Entity):

    def basic_attack(self, hero):
        if hero.get_hp() > 0:
            damage = randrange(2, 5)
            hero.take_damage(damage)
            print(f"\n~{damage}DMG\nYou've been hit by the dragons tail!\n")
        else:
            print("Game Over")

    def special_attack(self, hero):
        if hero.get_hp() > 0:
            damage = randrange(3, 7)
            hero.take_damage(damage)
            print(f"\n~{damage}DMG\n You've been struck by the dragons claw\n")
        else:
            print("Game Over")

    def random_attack(self, hero):
        attack = random.choice([self.basic_attack, self.special_attack])
        if hero.get_hp() > 0:
            attack(hero)
