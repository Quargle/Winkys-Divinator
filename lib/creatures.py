
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
        self.attack_bonus = self.set_attack_bonus()
        self.damage_bonus = self.set_damage_bonus()


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

    def set_attack_bonus(self):
        if "Finesse" in self.weapon.properties:
            ability_mod = max(self.str_mod, self.dex_mod)
        else:
            ability_mod = self.str_mod
        return (ability_mod + self.proficiency_bonus)

    def set_damage_bonus(self):
        if "Finesse"  in self.weapon.properties:
            damage_bonus = max(self.str_mod, self.dex_mod)
        else:
            damage_bonus = self.str_mod



class Fighter(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_HP = 10 + self.con_mod + ((4 + self.con_mod) * (self.level - 1))
        self.fighting_style = "Duellist"

    def __repr__(self):
        return f"""
                    {self.name} is a Level {self.level} Fighter.
                    Max HP: {self.max_HP}
                    Strength: {self.str}
                    Dexterity: {self.dex}
                    Constitution: {self.con}
                    Armor: {self.armor.name}
                    AC: {self.AC}
                    Weapon: {self.weapon.name}  

                """
# TODO: Add fighting styles


class Barbarian(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_HP = 12 + self.con_mod + ((4 + self.con_mod) * (self.level - 1))
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
                    Max HP: {self.max_HP}
                    Strength: {self.str}
                    Dexterity: {self.dex}
                    Constitution: {self.con}
                    Armor: {self.armor.name}
                    AC: {self.AC}
                    Weapon: {self.weapon.name}

                """


