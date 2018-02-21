#!/usr/bin/env python
"""Plot CSV visualizes CSV data."""

# plotcsv.py
# Plot CSV v1.0

# Michael McMahon

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
    description='Plot CSV visualizes csv data using matplotlib.')
PARSER.add_argument('csvfile', metavar='N', type=str,
                    help='a csv spreadsheet to be graphed')
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
    plt.xlabel('Events')
    plt.ylabel('Score')
    plt.title(csv_input)
    plt.legend(loc='upper left')

    # Save output as png.
    plt.savefig(csv_input+'.png')


if __name__ == '__main__':
    plotaspng(FILE)
