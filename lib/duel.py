#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    This module runs the duel mode.
"""

import lib.character as char


def main(character_1, character_2):
    char_1 = char.Character(
        DnD_class=character_1['class'],
        race=character_1['race'],
        weapon=character_1['weapon']
    )
    char_2 = char.Character(
        DnD_class=character_2['class'],
        race=character_2['race'],
        weapon=character_2['weapon']
    )




# For testing only
if __name__ == "__main__":
    main(
        name="Bob",
        age=23,
    )

