#!/usr/bin/env python
"""Plot CSV visualizes CSV data."""

# plotcsv.py
# Plot CSV v1.0.0
# Copyright (C) 2017-2020 Michael McMahon

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Plot CSV uses python 3 because of the dependencies.  Tested with v3.5.2.

# Run with this command:
#   python3 plotcsv.py INSERTCSVFILENAMEHERE
#
# View help:
#   python3 plotcsv.py -h

# Install dependencies
#  pip3 install matplotlib --upgrade
#  pip3 install pandas --upgrade

# Resources
# Ex 3 http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.savefig.html
# https://matplotlib.org/examples/pylab_examples/plotfile_demo.html
# From ars at https://stackoverflow.com/questions/1186789

# Import libraries
import argparse  # Add switch arguments for python v2.7 and v3.2+

# argparse
# This section adds switch -h and argument to the script.
PARSER = argparse.ArgumentParser(
    description="Plot CSV visualizes csv data using matplotlib."
)
PARSER.add_argument(
    "csvfile", metavar="N", type=str, help="a csv spreadsheet to be graphed"
)
ARGS = PARSER.parse_args()

# Variables
FILE = ARGS.csvfile

# Plot csv spreadsheet as png picture module


def plotaspng(csv_input):
    """Plot csv spreadsheet as png picture module."""
    # Import modules
    import matplotlib.pyplot as plt  # Plotting
    import pandas as pd  # Data Analysis

    # Read from csv file
    dfp = pd.read_csv(csv_input, index_col=0)

    # Plot data from csv
    dfp.plot(x=dfp.index, y=dfp.columns)

    plt.figure()
    dfp.plot()

    # Graph labels
    plt.xlabel("Events")
    plt.ylabel("Score")
    plt.title(csv_input)
    plt.legend(loc="upper left")

    # Save output as png.
    plt.savefig(csv_input + ".png")


if __name__ == "__main__":
    plotaspng(FILE)
