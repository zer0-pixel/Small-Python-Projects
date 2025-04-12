from pokemon import Pokemon
import random
from random import randrange

class Water(Pokemon):
    def __init__(self, name = "Lapras", poke_type="Water/Ice"):
        super().__init__(name, poke_type)
        self._special_1 = "Hydropump"
        self._special_2 = "Aurora Beam"
        self._opp_special_1 = "Water Gun"
        self._opp_special_2 = "Surf"

    def get_special_menu(self):
        return (f"1. {self._special_1} | 50 - 120 DMG\n"
                f"2. {self._special_2} | 30 - 65 DMG")

    def _special_move(self, opponent, move):
        damage = 0
        effect = ""

        if move == self._special_1:
            if opponent._poke_type == "Fire":
                damage = randrange(5, 13)
                effect = "It's Super Effective!"
            elif opponent._poke_type == "Grass":
                damage = randrange(2, 4)
                effect = "Not Very Effective..."
            else:
                damage = randrange(3,7 )

        elif move == self._special_2:
            if opponent._poke_type == "Fire":
                damage = randrange(5, 11)
                effect = "Its Super Effective!"
            elif opponent._poke_type =="Grass":
                damage = randrange(1, 3)
                effect = "Not Very Effective..."
            else:
                damage = randrange(4, 7)
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
                damage = randrange(5, 7)
                effect = "It's Super Effective!"
            elif player._poke_type == "Grass":
                damage = randrange(1, 3)
                effect = "Not Very Effective..."
            else:
                damage = randrange(2, 8)
        if opp_attack == self._opp_special_2:
            if player._poke_type == "Fire":
                damage = randrange(5,9)
                effect = "It's Super Effective!"
            elif player._poke_type == "Grass":
                damage = randrange(1,4)
                effect = "Not Very Effective..."
            else:
                damage = randrange(2,6)

        player._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {player._name}! {effect}\n"

