#!/usr/bin/python3
# -*- coding: utf-8 -*-
#*****************************************************************************************
# Characters.py
# Python 3
# Peter Evans, October 2018
# Initialises Characters for DND Duels
#********************************************************************************

from Old.character import Barbarian, Fighter
from .weapons import *
from.armor import *

def initialise_characters():
    # Attributes to enter are: (name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, features)
    Amber = Fighter("Amber", "Mountain Dwarf", "Fighter", 1, Maul, Chainmail, 16, 12, 16, [], ["Great Weapon Fighting"])
    Hermann = Fighter("Hermann", "Half-Orc", "Fighter", 2, Longsword, Chainmail, 16, 10, 16, ["Shield"], ["Duellist"])
    Alcazar = Barbarian("Alcazar", "Half-Orc", "Barbarian", 1, Greataxe, Unarmored, 16, 12, 16, [], [])