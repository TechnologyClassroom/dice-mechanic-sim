# dice-mechanic-sim
DMS tests game mechanics for Midnight Riders, the upcoming pen and paper RPG.

Michael McMahon

This code is released under the [AGPL 3.0 license](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/LICENSE).

This script can be used to balance dice based RPGs and board games.

DMS boils the game down to only the game mechanics by removing the theme and the characters.

Tested with python versions 3.5.2, but should work with 3.2+.

<a href="https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/changelog.txt">Change log</a>

## How to install Python

  * GNU/Linux Installation Instructions

Python is probably already installed on your GNU/Linux system.  You can check that Python is installed by running this command from a terminal:

```
python3 -V
```

Install all dependencies for Debian 9

```
apt install -y python3-pip
apt install -y python3-tk
pip3 install pandas
pip3 install matplotlib
apt install -y gpicview
apt install -y zip
```

  * Mac Installation Instructions

Python is already installed on your system.  You can check that Python is installed by running this command from the terminal:

```
python3 -V
```

If you would like to use IDLE, install [version 3 from python.org](https://www.python.org/downloads/mac-osx/).  

  * Windows Installation Instructions

The easiest way to install Python (and many other common programs) for Windows is through <a href="https://ninite.com/python/">ninite.  Ninite</a> is a website that allows you to install many programs at once without accidentally installing adware.  The ninite download program can be left on your system and used as an updater in the future.

## How to run this script

Install python.  Download this script.  Open a terminal.  Change to the directory with the script.

Run with this command:

```python3 dicemechanicsim.py```

View help:

```python3 dicemechanicsim.py -h```

Enable verbose mode:

```python3 dicemechanicsim.py -v```

Loop the script every two seconds (GNU/Linux or UNIX):

```watch -n 2 python3 dicemechanicsim.py```

Loop the script 40 times and packages as a data pack (GNU/Linux or UNIX):

```bash builddatapack.sh```

Alternatively, open the file in IDLE, make changes, save, and press F5 to run the script.

## Features

-The game results are recorded into a .csv file

-The script works on all major operating systems (GNU/Linux, Mac, UNIX, and Windows)

-No AI is present.  All decisions are made randomly.

-Static choices can be selected for player 1, late game, and all players for NPC interactions.

-The simulation runs in milliseconds instead of hours.  This allows for fast experimentation with rule changes instead of months of gameplay tests.

Feature requests can be found in the <a href="https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md">goals.md file</a>.

# How to analyze data generated from this script

Open the [data folder](https://github.com/TechnologyClassroom/dice-mechanic-sim/tree/master/data), download, and extract a data pack for example data.

What is a CSV file?  CSV stands for comma separated values.  It is a very simple spreadsheet with each row being a new line and each column separated by commas.

The csv files can be opened with popular spreadsheet software such as LibreOffice Calc or Microsoft Excel.  A plain text editor can also view the files quickly.

Data analysis software and programming languages can be used to parse the data.

Data can be graphed with spreadsheet software or within python through matplotlib, plotly, networkx, or igraph.

## Game Logic

The logic behind the game can be seen in the [gamelogic.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/gamelogic.md).

## Goals

Goals for the project can be found in the [goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

## Contributing

[*Imposter syndrome disclaimer*](https://github.com/adriennefriend/imposter-syndrome-disclaimer): I want your help.  No really, I do.

See the [CONTRIBUTING.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/CONTRIBUTING.md) for loose guidelines on how you can help.
