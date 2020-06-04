#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    This module runs the duel mode.
"""

# local imports
from . import creatures, var
from .roll import d4, d6, d8, d10, d12, d20


def create_duellists(form):
    char_class = {
        "Fighter": creatures.Fighter,
        "Barbarian": creatures.Barbarian,
    }
    char1 = char_class[form.char1_class.data](
            name=form.char1_name.data,
            level=form.char1_level.data,
        )
    char2 = char_class[form.char2_class.data](
            name=form.char2_name.data,
            level=form.char2_level.data,
        )
    return char1, char2


def main(form):
    char1, char2 = create_duellists(form)
    var.output = []
    print(char1.__repr__())
    var.output.append(char1.__repr__())
    print(char2.__repr__())
    var.output.append(char2.__repr__())


