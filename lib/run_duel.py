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
            str=char.str.data,
            dex=char.dex.data,
            con=char.con.data,
            off_hand=char.off_hand.data,
            armor=char.armor.data,
        )
    return character


def sort_initiative(char1, char2):
    """
        Determine the initiative order, re-rolling on a tie
        :param char1: The first character object
        :param char2: The second character object
        :return: a tuple containing the two character objects in initiative order
    """
    char1_initiative = char2_initiative = 0
    while char1_initiative == char2_initiative:
        char1_initiative = char1.roll_initiative()
        char2_initiative = char2.roll_initiative()
    if char1_initiative > char2_initiative:
        return char1, char2
    else:
        return char2, char1


def fight(char1, char2):
    # sort initiative:
    first, second = sort_initiative(char1, char2)
    var.output.append(f"{first.name} has won the initiative roll, and will go first!")
    var.output.append("")
    # Take Turns:
    var.turn_counter = 1
    while (first.HP > 0) and (second.HP > 0):
        var.output.append(f"Turn {var.turn_counter}:")
        first.take_turn(target=second)
        if second.HP > 0:
            second.take_turn(target=first)
        var.turn_counter += 1
    output = var.output # This is called for debugging purposes
    if first.HP > 0:
        var.output.append(f"{first.name} wins the Duel!")
    else:
        var.output.append(f"{second.name} wins the Duel!")



def main(form):
    char1 = create_duellist(form.char1)
    char2 = create_duellist(form.char2)
    var.output = []
    fight(char1, char2)
    print(char1.__repr__())
    print(char2.__repr__())
    return char1, char2


