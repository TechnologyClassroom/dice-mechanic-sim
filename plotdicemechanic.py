#!/usr/bin/env python
"""PDM visualizes Midnight Riders csv data using matplotlib."""

# plotdicemechanic.py
# Plot Dice Mechanic v1.1.0

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

# Another version of PDM exists that can take arguments.
# Find plotcsv.py at
# https://github.com/TechnologyClassroom/dice-mechanic-datapacks/blob/master/plotcsv.py

# PDM tested with python 3.5.2, pandas 0.20.3, matplotlib 2.1.0, and Debian 9.

# Run with this command:
#   python3 plotdicemechanicsim.py

# Install dependencies
#  pip3 install matplotlib
#  pip3 install numpy==1.15.0
#  pip3 install pandas==0.20.3

# Resources
# Ex 3 http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.savefig.html
# https://matplotlib.org/examples/pylab_examples/plotfile_demo.html
# From ars at https://stackoverflow.com/questions/1186789


# Variables
EXAMPLECSV = "data/20180219214011.csv"


def plotaspng(csvfile):
    """Plot csv spreadsheet as png picture module."""
    # Import modules

    # Force matplotlib to not use the Xwindows backend
    from matplotlib import use  # Plotting

    use("Agg")

    import matplotlib.pyplot as plt  # Plotting
    import pandas as pd  # Data Analysis

    # (Optional) xkcd format
    # plt.xkcd()

    # Read from csv file
    dfp = pd.read_csv(csvfile, index_col=0)

    # New versions of pandas have trouble understanding the index.

    # Plot data from csv
    dfp.plot(x=dfp.index, y=dfp.columns)

    plt.figure()
    dfp.plot()

    # Graph labels
    plt.xlabel("Events")
    plt.ylabel("Score")
    plt.title(csvfile)
    plt.legend(loc="upper left")

    # Save output as png.
    plt.savefig(csvfile + ".png")


if __name__ == "__main__":
    plotaspng(EXAMPLECSV)
