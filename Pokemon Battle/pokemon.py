from random import randrange
import abc

class Pokemon(abc.ABC):
    def __init__(self, name, p_type):
        self._name = name
        self._poke_type = p_type
        self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
        self._hp = 25

    @property
    def hp(self):
        return self._hp

    def get_normal_menus(self):
        return ("\n1. Slam | 2 - 7 DMG\n"
                "2. Tackle | 3 - 7 DMG")

    def _normal_move(self, opponent, move):
        move = self._slam(opponent) or self._tackle(opponent)
        return f"{move}"

    def _slam(self, opponent):
        damage = randrange(2, 40)
        opponent._take_damage(damage)
        return f"{self._name} used Slam and dealt {damage}DMG to {opponent._name}!"

    def _tackle(self, opponent):
        damage = randrange(3, 35)
        opponent._take_damage(damage)
        return f"{self._name} used Tackle and dealt {damage}DMG to {opponent._name}!"

    def _opp_Body_slam(self, player, move):
        damage = randrange(2, 4)
        player._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {player._name}!\n"

    def _opp_Bite(self, player, move):
        damage = randrange(3,6)
        player._take_damage(damage)
        return f"\n{self._name} used {move} and dealt {damage} DMG to {player._name}!\n"

    @abc.abstractmethod
    def get_special_menu(self):
        pass

    @abc.abstractmethod
    def _special_move(self, opponent, move):
        pass

    def attack(self, opponent, type, move):
        if type == "normal":
            return self._normal_move(opponent, move)
        elif type == "special":
            return self._special_move(opponent, move)


    def __str__(self):
        return f"{self._name}: HP/{self._hp} | {self._poke_type} "

    def _take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0







