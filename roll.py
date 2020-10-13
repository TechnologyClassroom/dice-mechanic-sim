#!/usr/bin/env python
"""roll simulates rolling polyhedral dice."""

# roll.py
# Roll v1.0.0
# Michael McMahon

from random import randrange

# Die roll function
# This function rolls a polyhedral die.
# Example: To roll an eight sided die (d8), use roll(8).


def roll(diefaces):
    """Simulate rolling a polyhedral die"""
    assert isinstance(diefaces, int) and diefaces >= 1
    return randrange(1, int(diefaces + 1))

# print(roll(20))  # Debug
