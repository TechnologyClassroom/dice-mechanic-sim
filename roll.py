#!/usr/bin/env python
"""roll simulates rolling polyhedral dice."""

# roll.py
# roll v1.0

# Michael McMahon

from random import randrange

# Die roll function
# This function rolls polyhedral dice.  Example: To roll a d8, use roll(8).


def roll(diefaces):
    """Simulate rolling polyhedral dice"""
    assert isinstance(diefaces, int) and diefaces >= 1
    return randrange(1, int(diefaces + 1))
