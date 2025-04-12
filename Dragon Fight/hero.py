from random import randrange
from entity import Entity

class Hero(Entity):
    def sword_attack(self, dragon):
        if dragon.get_hp() > 0:
            damage = randrange(1, 7)
            dragon.take_damage(damage)
            print(f"~-{damage}DMG~\nYou hit the dragon!")
        elif dragon.get_hp() <= 0:
            print(f"You've Defeated the {dragon.get_name()}!")

    def arrow_attack(self, dragon):
        if dragon.get_hp() > 0:
            damage = randrange(1, 13)
            dragon.take_damage(damage)
            print(f"~-{damage}DMG\nYou shot the dragon!")
        elif dragon.get_hp() <= 0:
            print(f"You've Defeated the {dragon.get_name()}!")
