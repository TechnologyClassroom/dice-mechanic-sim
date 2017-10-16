# plotdicemechanic.py
# Plot Dice Mechanic v1.0

# Michael McMahon

# PDM Visualize csv data with plotly for Midnight Riders.

# Tested with python 3 and matplotlib 2.1.0

# PDM uses python 3 because of the dependencies.  Tested with v3.5.2.


# Install dependencies
#  pip3 install matplotlib --upgrade
#  pip3 install pandas --upgrade
#  Additional system dependencies may be needed for Debian:
#    apt-get install -y libpng12-dev libfreetype6-dev pkg-config
#    apt-get install -y libffi-dev
#    pip3 install cairocffi
#    apt-get install python-gobject-cairo

# Resources
# Example 3 http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.savefig.html
# https://matplotlib.org/examples/pylab_examples/plotfile_demo.html
# From ars at https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script

# Variables

file = '20171016141044.csv'


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

