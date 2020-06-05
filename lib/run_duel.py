#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    This module runs the duel mode.
"""

# local imports
from . import creatures, var
from .roll import d4, d6, d8, d10, d12, d20


def create_duellist(char):
    char_class = {
        "Fighter": creatures.Fighter,
        "Barbarian": creatures.Barbarian,
    }
    character = char_class[char.char_class.data](
            name=char.char_name.data,
            level=char.level.data,
            race=char.race.data,
            weapon=char.weapon.data,
            armor=char.armor.data,
        )
    return character


def main(form):
    char1 = create_duellist(form.char1)
    char2 = create_duellist(form.char2)
    var.output = {}
    print(char1.__repr__())
    print(char2.__repr__())
    print(char1.__class__.__name__)
    return char1, char2


