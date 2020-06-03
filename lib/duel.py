#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    This module runs the duel mode.
"""

import lib.character


def main(**kwargs):
    print("The arguments passed are:")
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


# For testing only
if __name__ == "__main__":
    main(
        name="Bob",
        age=23,
    )

