#!/usr/bin/env python
"""roll simulates rolling polyhedral dice."""

# roll.py
# Roll v1.0.0

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


from random import randrange

# Die roll function
# This function rolls a polyhedral die.
# Example: To roll an eight sided die (d8), use roll(8).


def roll(diefaces):
    """Simulate rolling a polyhedral die"""
    assert isinstance(diefaces, int) and diefaces >= 1
    return randrange(1, int(diefaces + 1))

# print(roll(20))  # Debug
