from pokemon import Pokemon
import random
from random import randrange

class Grass(Pokemon):
    def __init__(self, name = "Ivysaur", poke_type="Grass/Poison"):
        super().__init__(name, poke_type)
        self._special_1 = "Mega Drain"
        self._special_2 = "Solar Beam"
        self._opp_special_1 = "Absorb"
        self._opp_special_2 = "Razor Leaf"

    def get_special_menu(self):
        return (f"1. {self._special_1} | 20 - 40 DMG\n"
                f"2. {self._special_2} | 50 - 120 DMG")

    def _special_move(self, opponent, move):
        damage = 0
        effect = ""

        if move == self._special_1:
            if opponent._poke_type == "Fire":
                damage = randrange(2, 4)
                effect = "Not Very Effective..."
            elif opponent._poke_type == "Water":
                damage = randrange(3, 13)
                effect = "It's Super Effective!"
            else:
                damage = randrange(4, 6)

        elif move == self._special_2:
            if opponent._poke_type == "Fire":
                damage = randrange(1, 3)
                effect = "Not Very Effective..."
            elif opponent._poke_type == "Water":
                damage = randrange(3, 11)
                effect = "It's Super Effective!"
            else:
                damage = randrange(3, 7)
        else:
            return f"Invalid Move! Please choose {self._special_1} or {self._special_2}."

        opponent._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {opponent._name}. {effect}"

    def opponent(self, player, move):
        opp_attack = random.choice([self._opp_special_1, self._opp_special_2])
        damage = 0
        effect = ""
        if opp_attack == self._opp_special_1:
            if player._poke_type == "Fire":
                damage = randrange(2, 4)
                effect = f"Not Very Effective.... +{damage}HP!"
                self._hp += damage
            elif player._poke_type == "Water":
                damage = randrange(5, 8)
                effect = f"It's Super Effective! +{damage}HP!"
                self._hp += damage
            else:
                damage = randrange(3, 6)
                effect = f"+{damage}HP!"
                self._hp += damage

        elif opp_attack == self._opp_special_2:
            if player._poke_type == "Fire":
                damage = randrange(1, 3)
                effect = "Not Very Effective..."
            elif player._poke_type == "Water":
                damage = randrange(3, 9)
                effect = "It's Super Effective!"
            else:
                damage = randrange(2, 5)


        player._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {player._name}! {effect}\n"




