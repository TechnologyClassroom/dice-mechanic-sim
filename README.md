# dice-mechanic-sim

Dice Mechanic Simulator (DMS) tests game mechanics for
[Midnight Riders](https://github.com/GhostCityGames/Midnight-Riders), the pen
and paper tabletop role-playing game (TTRPG).

Michael McMahon

Thank you for visiting us at the [World Maker Faire 2018](https://makerfaire.com/new-york/)
at the location 3 tent in the games section!

Support the developers of Midnight Riders by purchasing a physical zine with
[our GCG Square Store](https://squareup.com/store/ghostcitygames/),
purchasing an ebook at
[DriveThruRPG](http://www.drivethrurpg.com/product/225714/Midnight-Riders), or
developing with us on
[Github](https://github.com/GhostCityGames/Midnight-Riders).

[![asciicast](https://github.com/TechnologyClassroom/dice-mechanic-datapacks/blob/master/gifs/mr.gif?raw=true)](https://asciinema.org/a/182976)

![Screenshot](https://github.com/TechnologyClassroom/dice-mechanic-datapacks/blob/master/20180219214011.csv.png?raw=true "Plot of 20180219214011.csv")

This code is released under the
[GNU Affero General Public License version 3 or any later version (AGPL-3.0-or-later) license](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/LICENSE).

[Slides](https://github.com/TechnologyClassroom/dice-mechanic-datapacks/blob/master/slides/README.md)
from talks regarding Midnight Riders can be found in the
[dice-mechanic-datapacks](https://github.com/TechnologyClassroom/dice-mechanic-datapacks)
repository.

This script can be used to balance dice based RPGs and board games.

DMS boils the game down to only the game mechanics by removing theme,
characters, and storytelling.

[Change log](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/changelog.txt)

## Game Logic

The logic behind the game can be seen in the
[gamelogic.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/gamelogic.md)
and is the fastest way to catch up if you are not familiar with the rules of
[Midnight Riders](https://github.com/GhostCityGames/Midnight-Riders).

## Goals

Goals for the project can be found in the
[goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

## Contributing

[*Imposter syndrome disclaimer*](https://github.com/adriennefriend/imposter-syndrome-disclaimer):
I want your help.  No really, I do.

See the
[CONTRIBUTING.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/CONTRIBUTING.md)
for loose guidelines on how you can help.

## How to setup a development environment

- GNU/Linux Installation Instructions

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
pip3 install numpy==1.15.0
pip3 install pandas==0.20.3
pip3 install matplotlib
apt install -y gpicview
apt install -y zip
```

Configure tox testing environment

```
bash buildtoxtestenvironment.sh
```

- Mac Installation Instructions

To install the dependencies, you need [homebrew](http://brew.sh/) which requires
[XCode](http://developer.apple.com/xcode/) which requires the latest macOS.
Apple should serve snapshots of older XCode packages for old releases purely for
this reason.  If your computer cannot run the latest macOS, I would suggest
[dual-booting GNU/Linux using this guide](https://github.com/TechnologyClassroom/SetupNotes/blob/master/GNULinux/GNULinuxOnMacbooks.md)
 or using a [Virtual Machine (VM)](https://www.virtualbox.org/wiki/Downloads)
instead of trading in for a new Mac.

Try to run the dicemechanicsim.py and solve each dependency.

- Windows Installation Instructions

The easiest way to install Python (and many other common programs) for Windows
is through [ninite.  Ninite](https://ninite.com/python/) is a website that
allows you to install many programs at once without accidentally installing
adware.  The ninite download program can be left on your system and used as an
updater in the future.

For all python files, use Notepad++ to change the end of line from UNIX / OS X
Format to Windows Format.

Try to run the dicemechanicsim.py and solve each dependency.

- If DMS is not compatible with your system...

You can setup a Debian Virtual Machine (VM) or I can upload a Debian VM that is
configured with all of the dependencies for you.

## How to run this script

Install python.  Download this script.  Open a terminal.  Change to the
directory with the script.

Run with this command:

```
python3 dicemechanicsim.py
```

View help:

```
python3 dicemechanicsim.py -h
```

Enable verbose mode:

```
python3 dicemechanicsim.py -v
```

Loop the script every two seconds (GNU/Linux or UNIX):

```
watch -n 2 python3 dicemechanicsim.py
```

Loop the script 40 times and package the results as a data pack (GNU/Linux or
UNIX):

```
bash builddatapack.sh
```

Alternatively, open the file in IDLE, make changes, save, and press F5 to run
the script.

## Features

- The game results are recorded as a spreadsheet in csv format and as a graph in
  png format.
- No AI is present yet.  All decisions are made randomly.
- Static choices can be selected for player 1, late game, and all players for
  NPC interactions.
- The simulation runs in milliseconds instead of hours.  This allows for fast
  experimentation with rule changes instead of months of gameplay tests.

Feature requests can be found in the
[goals.md file](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md).

## How to analyze data generated from this script

Note: Programming experience is not required to participate with data analysis.

Open the
[dice-mechanic-datapacks repository](https://github.com/TechnologyClassroom/dice-mechanic-datapacks),
download, and extract the most recent data pack for example data.

What is a CSV file?  CSV stands for comma separated values.  It is a very simple
spreadsheet with each row being a new line and each column separated by commas.

The csv files can be opened with popular spreadsheet software such as
LibreOffice Calc or Microsoft Excel.  A plain text editor can also view the
files quickly.

Data analysis software and programming languages can be used to parse the data.

Data is graphed within python through pandas and matplotlib.
