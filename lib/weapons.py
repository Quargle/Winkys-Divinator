# -*- coding: utf-8 -*-

from random import randint


class Weapon:
    def __init__(self, name, damage, damage_type, properties):
        self.name = name
        self.damage = damage
        self.damage_dice = int(self.damage.split('d')[0])
        self.damage_die = int(self.damage.split('d')[1])

        self.damage_type = damage_type
        self.properties = properties

    def describe(self):
        print("Name: {}  Damage: {}  Properties: ".format(self.name, self.damage, self.properties))

    def roll_damage(self, crit=False):
        rolls = []
        dice = self.damage_dice
        if crit:
            dice *= 2
        for _ in range(dice):
            rolls.append(randint(1, self.damage_die))
        return rolls


weapon_dict = {
    "Club": Weapon("Club", "1d4", "Bludgeoning", ["Light"]),
    "Dagger": Weapon("Dagger", "1d4", "Piercing", ["Light", "Finesse"]),
    "Greatclub": Weapon("Greatclub", "1d8", "Bludgeoning", ["2-handed"]),
    "Handaxe": Weapon("Handaxe", "1d6", "Slashing", ["Light"]),
    "Javelin": Weapon("Javelin", "1d6", "Piercing", []),
    "Light Hammer": Weapon("Light Hammer", "1d6", "Bludgeoning", ["Light"]),
    "Mace": Weapon("Mace", "1d6", "Bludgeoning", []),
    "Quarterstaff": Weapon("Quarterstaff", "1d6", "Bludgeoning", ["Versatile"]),
    "Sickle": Weapon("Sickle", "1d4", "Slashing", ["Light"]),
    "Spear": Weapon("Spear", "1d6", "Piercing", ["Versatile"]),
    "Battleaxe": Weapon("Battleaxe", "1d8", "Slashing", ["Versatile"]),
    "Flail": Weapon("Flail", "1d8", "Bludgeoning", []),
    "Glaive": Weapon("Glaive", "1d10", "Slashing", ["Heavy", "2-handed"]),
    "Greataxe": Weapon("Greataxe", "1d12", "Slashing", ["Heavy", "2-handed"]),
    "Greatsword": Weapon("Greatsword", "2d6", "Slashing", ["Heavy", "2-handed"]),
    "Halberd": Weapon("Halberd", "1d10", "Slashing", ["Heavy", "2-handed"]),
    "Lance": Weapon("Lance", "1d12", "Piercing", ["Special"]),
    "Longsword": Weapon("Longsword", "1d8", "Slashing", ["Versatile"]),
    "Maul": Weapon("Maul", "2d6", "Bludgeoning", ["2-handed"]),
    "Morningstar": Weapon("Morningstar", "1d8", "Piercing", []),
    "Pike": Weapon("Pike", "1d10", "Piercing", ["Heavy", "2-handed"]),
    "Rapier": Weapon("Rapier", "1d8", "Piercing", ["Finesse"]),
    "Scimitar": Weapon("Scimitar", "1d6", "Slashing", ["Finesse", "Light"]),
    "Shortsword": Weapon("Shortsword", "1d6", "Piercing", ["Finesse", "Light"]),
    "Trident": Weapon("Trident", "1d6", "Piercing", ["Versatile"]),
    "War Pick": Weapon("War Pick", "1d8", "Piercing", []),
    "Warhammer": Weapon("Warhammer", "1d8", "Bludgeoning", ["Versatile"]),
    "Whip": Weapon("Whip", "1d4", "Slashing", ["Finesse"]),
    "Unarmed_Strike": Weapon("Unarmed Strike", "1d4", "Bludgeoning", ["Unarmed"]),
}
