#!/usr/bin/env python
"""roll simulates rolling polyhedral dice."""
# roll.py

# Michael McMahon

from random import randrange

# Die roll function
# This function rolls polyhedral dice.  Example: To roll a d8, use roll(8).


def roll(diefaces):
    """Simulate rolling polyhedral dice"""
    return randrange(1, int(diefaces + 1))
