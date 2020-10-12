#!/usr/bin/env py.test
"""py.test for roll.py"""

from pytest import raises
from roll import roll


def test_range_common_dice():
    """Test whether all common polyhedral dice roll within their range"""
    # Test depends on random number and is not repeatable.
    common_dice = [4, 6, 8, 10, 12, 20]
    for dice in common_dice:
        for _ in range(0, 99):
            assert 1 <= roll(dice) <= dice


def test_range_uncommon_dice():
    """Test whether uncommon polyhedral dice roll within their range"""
    # Test depends on random number and is not repeatable.
    common_dice = [3, 5, 7, 14, 16, 18, 22, 24, 50, 60, 100]
    for dice in common_dice:
        for _ in range(0, 99):
            assert 1 <= roll(dice) <= dice


def test_range_d1():
    """Test whether a one sided die will always land on 1"""
    assert roll(1) == 1


def test_negative_integer():
    """Test whether rolling a negative number generates an Exception"""
    with raises(AssertionError):
        roll(-1)


def test_string():
    """Test whether rolling a string generates an Exception"""
    with raises(AssertionError):
        roll(str("Hello, World!"))
