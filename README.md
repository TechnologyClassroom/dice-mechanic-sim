# dice-mechanic-sim
Dice Mechanic Simulator (DMS) tests game mechanics for Midnight Riders, the pen
and paper RPG.

Michael McMahon

Support the developers of Midnight Riders by purchasing a physical book at
[Etsy](https://www.etsy.com/listing/576575261/midnight-riders-role-playing-game),
an ebook at [DriveThruRPG](http://www.drivethrurpg.com/product/225714/Midnight-Riders),
or developing with us on [Github](https://github.com/GhostCityGames/Midnight-Riders).

![Screenshot](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/data/20171030125109.csv.png?raw=true "Plot of 20171030125109.csv")

This code is released under the [AGPL 3.0 license](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/LICENSE).

This script can be used to balance dice based RPGs and board games.

DMS boils the game down to only the game mechanics by removing the theme and the
characters.

[Change log](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/changelog.txt)

## How to setup a development environment

* GNU/Linux Installation Instructions

Python is probably already installed on your GNU/Linux system.  You can check if
Python is installed by running this command from a terminal:

```
python3 -V
```

Install all dependencies for Debian 9

```
apt update
apt install -y python3-pip
apt install -y python3-tk
pip3 install pandas
pip3 install matplotlib
apt install -y gpicview
apt install -y zip
```

* Mac Installation Instructions

To install the dependencies, you need [homebrew](http://brew.sh/) which requires
[XCode](http://developer.apple.com/xcode/) which requires the latest macOS.
Apple should serve snapshots of older XCode packages for old releases purely for
this reason.  If your computer cannot run the latest macOS, I would suggest
[dual-booting GNU/Linux using this guide](https://github.com/TechnologyClassroom/SetupNotes/blob/master/GNULinux/GNULinuxOnMacbooks.md)
or using a [Virtual Machine (VM)](https://www.virtualbox.org/wiki/Downloads)
instead of trading in for a new Mac.

Try to run the dicemechanicsim.py and solve each dependency.

* Windows Installation Instructions

The easiest way to install Python (and many other common programs) for Windows
is through <a href="https://ninite.com/python/">ninite.  Ninite</a> is a website
that allows you to install many programs at once without accidentally installing
adware.  The ninite download program can be left on your system and used as an
updater in the future.

Try to run the dicemechanicsim.py and solve each dependency.

* If DMS is not compatible with your system...

You can setup a Debian Virtual Machine (VM) or I can upload a Debian VM that is
configured with all of the dependencies for you.

## How to run this script

Install python.  Download this script.  Open a terminal.  Change to the
directory with the script.

Run with this command:

```python3 dicemechanicsim.py```

View help:

```python3 dicemechanicsim.py -h```

Enable verbose mode:

```python3 dicemechanicsim.py -v```

Loop the script every two seconds (GNU/Linux or UNIX):

```watch -n 2 python3 dicemechanicsim.py```

Loop the script 40 times and package the results as a data pack (GNU/Linux or
UNIX):

```bash builddatapack.sh```

Alternatively, open the file in IDLE, make changes, save, and press F5 to run
the script.

## Features

-The game results are recorded as a spreadsheet in csv format and as a graph in
png format.

-No AI is present yet.  All decisions are made randomly.

-Static choices can be selected for player 1, late game, and all players for NPC
interactions.

-The simulation runs in milliseconds instead of hours.  This allows for fast
experimentation with rule changes instead of months of gameplay tests.

Feature requests can be found in the [goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

# How to analyze data generated from this script

Note: Programming experience is not required to participate with data analysis.

Open the [data folder](https://github.com/TechnologyClassroom/dice-mechanic-sim/tree/master/data)
, download, and extract the most recent data pack for example data.

What is a CSV file?  CSV stands for comma separated values.  It is a very simple
spreadsheet with each row being a new line and each column separated by commas.

The csv files can be opened with popular spreadsheet software such as
LibreOffice Calc or Microsoft Excel.  A plain text editor can also view the
files quickly.

Data analysis software and programming languages can be used to parse the data.

Data is graphed within python through matplotlib.

## Game Logic

The logic behind the game can be seen in the [gamelogic.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/gamelogic.md).

## Goals

Goals for the project can be found in the [goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

## Contributing

[*Imposter syndrome disclaimer*](https://github.com/adriennefriend/imposter-syndrome-disclaimer):
I want your help.  No really, I do.

See the [CONTRIBUTING.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/CONTRIBUTING.md)
for loose guidelines on how you can help.
