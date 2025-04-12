
class Entity:
    def __init__(self, name,max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp

    def take_damage(self, damage):
        if damage > 0:
            self._hp -= damage
            if self._hp < 0:
                self._hp = 0

    def __str__(self):
        return f"{self._name}: {self._hp}/{self._max_hp}"





