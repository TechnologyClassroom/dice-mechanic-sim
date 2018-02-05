#!/usr/bin/env python
"""PDM visualizes Midnight Riders csv data using matplotlib."""

# plotdicemechanic.py
# Plot Dice Mechanic v1.0

# Michael McMahon

# Another version of PDM exists that can take arguments.
# Find plotcsv.py at
# https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/data/plotcsv.py

# Tested with python 3 and matplotlib 2.1.0

# PDM uses python 3 because of the dependencies.  Tested with v3.5.2.

# Run with this command:
#   python3 plotdicemechanicsim.py

# Install dependencies
#  pip3 install matplotlib --upgrade
#  pip3 install pandas --upgrade

# Resources
# Ex 3 http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.savefig.html
# https://matplotlib.org/examples/pylab_examples/plotfile_demo.html
# From ars at https://stackoverflow.com/questions/1186789

# Variables
EXAMPLECSV = 'data/20171030125109.csv'


def plotaspng(csvfile):
    """Plot csv spreadsheet as png picture module"""
    # Import modules
    import matplotlib.pyplot as plt  # Plotting
    import pandas as pd  # Data Analysis

    # (Optional) xkcd format
    # plt.xkcd()

    # Read from csv file
    dfp = pd.read_csv(csvfile, index_col=0)

    # Plot data from csv
    dfp.plot(x=dfp.index, y=dfp.columns)

    plt.figure()
    dfp.plot()

    # Graph labels
    plt.xlabel('Events')
    plt.ylabel('Score')
    plt.title(csvfile)
    plt.legend(loc='upper left')

    # Save output as png.
    plt.savefig(csvfile + '.png')


if __name__ == '__main__':
    plotaspng(EXAMPLECSV)
