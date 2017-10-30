# plotcsv.py
# Plot CSV v1.0

# Michael McMahon

# Plot CSV visualizes csv data using matplotlib.

# Tested with python 3 and matplotlib 2.1.0

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
# Example 3 http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.savefig.html
# https://matplotlib.org/examples/pylab_examples/plotfile_demo.html
# From ars at https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script

# Import libraries
import argparse  # Add switch arguments for python v2.7 and v3.2+

# argparse
# This section adds switch -h and argument to the script.
parser = argparse.ArgumentParser(
    description='Plot CSV visualizes csv data using matplotlib.')
parser.add_argument('csvfile', metavar='N', type=str,
                    help='a csv spreadsheet to be graphed')
args = parser.parse_args()

# Variables
file = args.csvfile

# Plot csv spreadsheet as png picture module
def plotaspng(input):
    # Import modules
    import pandas as pd  # Data Analysis
    import matplotlib.pyplot as plt  # Plotting

    # Read from csv file
    df = pd.read_csv(input, index_col=0)

    # Plot data from csv
    df.plot(x=df.index, y=df.columns)

    plt.figure()
    df.plot()

    # Graph labels
    plt.xlabel('Events')
    plt.ylabel('Score')
    plt.title(input)
    plt.legend(loc='upper left')

    # Save output as png.
    plt.savefig(input+'.png')

if __name__ == '__main__':
    plotaspng(file)
