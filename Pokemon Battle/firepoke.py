import random
from pokemon import Pokemon
from random import randrange

class Fire(Pokemon):
    def __init__(self, name = "Charizard", poke_type="Fire/Flying"):
        super().__init__(name, poke_type)
        self._special_1 = "Ember"
        self._special_2 = "Fire Blast"
        self._opp_special_1 = "Fire Punch"
        self._opp_special_2 = "Flamethrower"

    def get_special_menu(self):
        return (f"1. {self._special_1} | 20 - 40 DMG\n"
                f"2. {self._special_2} | 40 - 120 DMG")

    def _special_move(self, opponent, move):
        damage = 0
        effect = ""

        if move == self._special_1:
            if opponent._poke_type == "Water":
                damage = randrange(2, 3)
                effect = "Not Very Effective..."
            elif opponent._poke_type == "Grass":
                damage = randrange(8, 15)
                effect = "It's Super Effective!"
            else:
                damage = randrange(4, 10)

        elif move == self._special_2:
            if opponent._poke_type == "Water":
                damage = randrange(1, 4)
                effect = "Not Very Effective..."
            elif opponent._poke_type == "Grass":
                damage = randrange(7, 10)
                effect = "It's Super Effective!"
            else:
                damage = randrange(2,7 )
        else:
            return f"Invalid Move! Please choose {self._special_1} or {self._special_2}."

        opponent._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {opponent._name}! {effect}"

    def opponent(self, player, move):
        opp_attack = random.choice([self._opp_special_1, self._opp_special_2])
        damage = 0
        effect = ""
        if opp_attack == self._opp_special_1:
            if player._poke_type == "Water":
                damage = randrange(1, 4)
                effect = "Not Very Effective..."
            elif player._poke_type == "Grass":
                damage = randrange(5,8)
                effect = "It's Super Effective!"
            else:
                damage = randrange(3, 7)

        elif opp_attack == self._opp_special_2:
            if player._poke_type == "Water":
                damage = randrange(2, 3)
                effect = "Not Very Effective..."
            elif player._poke_type == "Grass":
                damage = randrange(4,10)
                effect = "It's Super Effective!"
            else:
                damage = randrange(3, 8)

        player._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {player._name}! {effect}\n"




