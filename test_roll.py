#!/usr/bin/env py.test
"""py.test for roll.py"""

# Copyright (C) 2017-2020 Michael McMahon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
