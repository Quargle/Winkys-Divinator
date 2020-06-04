
# Standard library imports
import math
#Local imports
from .roll import d4, d6, d8, d10, d12, d20
from . import armor, weapons

class Creature:
    def __init__(self, **kwargs):
        self.str = getattr(kwargs, 'str', 16)
        self.dex = getattr(kwargs, 'dex', 16)
        self.con = getattr(kwargs, 'con', 16)
        self.str_mod = self.set_ability_modifier(self.str)
        self.dex_mod = self.set_ability_modifier(self.dex)
        self.con_mod = self.set_ability_modifier(self.con)
        self.features = []

    @staticmethod
    def set_ability_modifier(ability_score):
        ability_mod = (ability_score - 10)/2
        return math.floor(ability_mod)

    def reset(self):
        self.HP = self.max_HP



class Character(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs['name']
        self.level = int(kwargs['level'])
        self.armor = armor.armor_dict[kwargs['armor']]
        self.weapon = weapons.weapon_dict[kwargs['weapon']]
        self.AC = self.set_AC()
        self.proficiency_bonus = self.set_proficiency_bonus()

    def set_AC(self):
        """ This method can be overriden by a subclass method where necessary"""
        return (self.armor.base_AC + min(self.dex_mod, self.armor.max_dex_bonus))

    def set_proficiency_bonus(self):
        if self.level < 5:
            proficiency_bonus = 2
        elif self.level < 9:
            proficiency_bonus = 3
        elif self.level < 13:
            proficiency_bonus = 4
        elif self.level < 17:
            proficiency_bonus = 5
        else:
            proficiency_bonus = 6
        return proficiency_bonus



class Fighter(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_HP = 10 + self.con + ((4 + self.con) * (self.level - 1))

    def __repr__(self):
        return f"""
                    {self.name} is a Level {self.level} Fighter.
                    Armor: {self.armor.name}
                    Strength: {self.str}
                    Dexterity: {self.dex}
                    Constitution: {self.con}
                """
# TODO: Add fighting styles


class Barbarian(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_HP = 12 + self.con + ((4 + self.con) * (self.level - 1))
        self.features.append("Rage")
        self.features.append("Unarmored Defense")
        if self.level >= 2:
            self.features.append("Reckless Attack")
            self.features.append("Danger Sense")
        if self.level >= 3:
            self.features.append("Frenzy")

    def set_AC(self):
        if self.armor.name == "Unarmored":
            return (10 + self.dex_mod + self.con_mod)
        else:
            return super().set_AC()

    def __repr__(self):
        return f"""
                    {self.name} is a Level {self.level} Barbarian.
                    Strength: {self.str}
                    Dexterity: {self.dex}
                    Constitution: {self.con}
                """


