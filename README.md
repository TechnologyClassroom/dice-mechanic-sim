# dice-mechanic-sim
DMS tests game mechanics for Midnight Riders, the upcoming pen and paper RPG.

Michael McMahon

This code is released under the [AGPL 3.0 license](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/LICENSE).

This script can be used to balance dice based RPGs and board games.

DMS boils the game down to only the game mechanics by removing the theme and the characters.

Tested with python versions 2.7.12 and 3.5.2, but should work with 2.7+ and 3.2+.7

<a href="https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/changelog.txt">Change log</a>

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

-Only native python libraries are required and no additional installations are necessary to run dicemechanicsim.py simulations.

-The script works on all major operating systems (GNU/Linux, Mac, UNIX, and Windows)

-No AI is present.  All decisions are made randomly.

-Static choices can be selected for player 1, late game, and all players.

-The simulation runs in milliseconds instead of hours.  This allows for fast experimentation with rule changes instead of months of gameplay tests.

Feature requests can be found in the <a href="https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md">goals.md file</a>.

# How to analyze data generated from this script

Open the [data folder](https://github.com/TechnologyClassroom/dice-mechanic-sim/tree/master/data), download, and extract a data pack for example data.

What is a CSV file?  CSV stands for comma separated values.  It is a very simple spreadsheet with each row being a new line and each column separated by commas.

The csv files can be opened with popular spreadsheet software such as LibreOffice Calc or Microsoft Excel.  A plain text editor can also view the files quickly.

Data analysis software and programming languages can be used to parse the data.

Data can be graphed with spreadsheet software or within python through matplotlib, plotly, networkx, or igraph.

# Game Logic

The logic behind the game can be seen in the [gamelogic.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/gamelogic.md).

# Goals

Goals for the project can be found in the [goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

# Contributing

[*Imposter syndrome disclaimer*](https://github.com/adriennefriend/imposter-syndrome-disclaimer): I want your help.  No really, I do.

See the [CONTRIBUTING.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/CONTRIBUTING.md) for loose guidelines to how you can help.
