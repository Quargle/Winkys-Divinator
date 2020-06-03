# -*- coding: utf-8 -*-

class Armor:
    def __init__(self, name, base_AC, type):
        self.name = name
        self.base_AC = base_AC
        self.type = type
        
        if self.type == "Light":
            self.max_dex_bonus = 7
        elif self.type == "Medium":
            self.max_dex_bonus = 2
        elif self.type == "Heavy":
            self.max_dex_bonus = 0


    def describe(self):
        print("Name: {}  Base AC: {}  Max Dexterity Bonus: ".format(self.name, self.base_AC, self.max_dex_bonus))


Unarmored = Armor("no armor", 10, "Light")
Leather = Armor("Leather", 11, "Light")
Studded_Leather = Armor("Studded Leather", 12, "Light")

Hide = Armor("Hide", 12, "Medium")
Chain_Shirt = Armor("Chain Shirt", 13, "Medium")
Scale_Mail = Armor("Scale Mail", 14, "Medium")
Breastplate = Armor("Breastplate", 14, "Medium")
Half_Plate = Armor("Half_Plate", 15, "Medium")

Chainmail = Armor("Chainmail", 16, "Heavy")
Splint = Armor("Splint", 17, "Heavy")
Full_Plate = Armor("Full Plate", 18, "Heavy")

Integrated_Heavy_Plating = Armor("Integrated Plate", 16, "Heavy")
