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
