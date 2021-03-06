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


armor_dict = {
    "No Armor": Armor("Unarmored", 10, "Light"),
    "Padded": Armor("Padded", 11, "Light"),
    "Leather": Armor("Leather", 11, "Light"),
    "Studded Leather": Armor("Studded Leather", 12, "Light"),
    "Hide": Armor("Hide", 12, "Medium"),
    "Chain Shirt": Armor("Chain Shirt", 13, "Medium"),
    "Scale Mail": Armor("Scale Mail", 14, "Medium"),
    "Breastplate": Armor("Breastplate", 14, "Medium"),
    "Half Plate": Armor("Half_Plate", 15, "Medium"),
    "Chain Mail": Armor("Chain Mail", 16, "Heavy"),
    "Splint Mail": Armor("Splint Mail", 17, "Heavy"),
    "Full Plate": Armor("Full Plate", 18, "Heavy"),
}


