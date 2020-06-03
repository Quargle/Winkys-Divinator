# -*- coding: utf-8 -*-

class Weapon:
    def __init__(self, name, damage, type, properties):
        self.name = name
        self.damage = damage
        self.properties = properties

    def describe(self):
        print("Name: {}  Damage: {}  Properties: ".format(self.name, self.damage, self.properties))



Unarmed_Strike = Weapon("Unarmed Strike", "1d4", "Bludgeoning", ["Unarmed"])
Quarterstaff = Weapon("Quarterstaff", "1d8", "Bludgeoning", ["Versatile"])
Shortsword = Weapon("Shortsword", "1d6", "Piercing", ["Finesse", "Light"])
Rapier = Weapon("Rapier", "1d8", "Piercing", ["Finesse"])
Flail = Weapon("Flail", "1d8", "Bludgeoning", [])
Longsword = Weapon("Longsword", "1d8", "Slashing", ["Versatile"])
Greatsword = Weapon("Greatsword", "2d6", "Slashing", ["2-handed"])
Maul = Weapon("Maul", "2d6", "Bludgeoning", ["2-handed"])
Greataxe = Weapon("Greataxe", "1d12", "Slashing", ["2-handed"])


