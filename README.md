# dice-mechanic-sim
DMS tests game mechanics for Midnight Riders, the upcoming pen and paper RPG.

Michael McMahon

This code is released under the AGPL 3.0.

This script can be used to balance dice based RPGs and board games.

No AI is present.  All decisions are made randomly.

Static choices can be selected for player 1.

The simulation runs in milliseconds instead of hours.  This allows for fast experimentation with rule changes instead of months of gameplay tests.

Tested with python versions 2.7.12 and 3.5.2, but should work with 2.7+ and 3.2+.

# How to run this script

Install python.  Download this script.  Open a terminal.  Change to the directory with the script.

Run with this command:

```python dicemechanicsim.py```

View help:

```python dicemechanicsim.py -h```

Enable verbose mode:

```python dicemechanicsim.py -v```

Loop the script every two seconds (GNU/Linux or UNIX):

```watch -n 2 python dicemechanicsim.py```

# Features

-The game results are recorded into a .csv file

-Only native python libraries are required.  No additional installations are necessary.

-The script works on all major operating systems (GNU/Linux, Mac, UNIX, and Windows)

# How to analyze data generated from this script

Open the data folder ( https://github.com/TechnologyClassroom/dice-mechanic-sim/tree/master/data ) and extract a data pack for example data.

What is a CSV file?  CSV stands for comma separated values.  It is a very simple spreadsheet with each row being a new line and each column separated by commas.

The csv files can be opened with popular spreadsheet software such as LibreOffice Calc or Microsoft Excel.  A plain text editor can also view the files.

Data analysis software and programming languages can also be used to parse the data.

Data can be graphed with spreadsheet software or with within python through plotly, pyplot, networkx, or igraph.
