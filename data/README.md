# Data packs

This folder will contain data sets for making informed decisions regarding rule
optimization.

Each data pack includes:
* Each csv file is a simulation of an entire game.  csv files are named with a
timestamp of when they were created.
* Plotted graph in png file.
* dicemechanicsim.py pyhon script with the same settings as the data

What is a CSV file?  CSV stands for comma separated values.  It is a very simple
spreadsheet with each row being a new line and each column separated by commas.
[This is an example of one csv file](https://raw.githubusercontent.com/TechnologyClassroom/dice-mechanic-sim/master/data/20171030125109.csv).

This is an example of a plot from a csv:
![Screenshot](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/data/20171030125109.csv.png?raw=true "Plot of 20171030125109.csv")

R1 is the Reputation score for Player 1.

M1 is the Madness score for Player 1.

R3 is the Reputation score for Player 3.

## How to analyze data generated in data packs

Download and extract a data pack for example data.

Ways to view and analyze the data:
* A plain text editor can also view the files quickly.
* The csv files can be opened with popular spreadsheet software such as
LibreOffice Calc, Google Sheets, or Microsoft Excel.
* Data can be graphed with spreadsheet software or within python through
matplotlib, plotly, networkx, or igraph.
* Data analysis software and programming languages can be used to parse the
data.

Goals for the data can be found in the [goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

## Observations and Findings

Observations and findings are recorded in the [analysis-observations](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/analysis-observations.md).

If you have any observations, you can submit them as a pull request or submit a
[new issue](https://github.com/TechnologyClassroom/dice-mechanic-sim/issues/new).
