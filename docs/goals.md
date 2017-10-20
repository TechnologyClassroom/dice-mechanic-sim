# Goals & Feature requests

# Game balance goals
Goals for the game mechanics to become more fun and balanced:

1) Numbers and dice should consistently increase as the game progresses

2) Close matches

3) High probability of event 7

4) Low probability of getting stuck at the first dice tier

5) Low probability of leaving a player left behind

Data analysis can be achieved by watching simulations over time and with data
analysis and graphing libraries (matplotlib).


# dicemechanicsim.py Feature requests
* Easy: Change code to [pep 8 style](https://www.python.org/dev/peps/pep-0008)
  * [Maximum line length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
  * A few automatic code analyzers are [autopep8](https://github.com/hhatto/autopep8),
   [yapf](https://github.com/google/yapf), and
   [pycodestyle](https://github.com/PyCQA/pycodestyle).
   of 80 characters per line for code and 72 for docstrings/comments.
* Easy: Only load pieces of libraries that are used to speed up processing time
* Easy: Run plotdicemechanic.py at the end of dicemechanicsim.py.
* Medium: Event 7 is a best 2 out of 3.
  * Best 2 out of 3
  * d12 to settle ties
* Medium: Event 7 edge cases need to be addressed
* Medium: Fight a random number of opponents
* Medium: Fake AI that makes better decisions than random
  * A new array could be created at the end of each conflict filled with each stat's
   dice tier.  When deciding an opponent, the new array could be analyzed for best points.
* Easy: Propose changes for dice tiers and points
* See tables section below
  * ~~Change point system for PC vs PC based on dice advantage~~
  * Medium: Relational NPC scoring with one point less than PC table scores
  * ~~Medium: Loss table~~
  * ~~Medium: Higher point table~~

# plotdicemechanic.py Feature requests
* Easy: Change code to [pep 8 style](https://www.python.org/dev/peps/pep-0008)
  * [Maximum line length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
  * A few automatic code analyzers are [autopep8](https://github.com/hhatto/autopep8),
   [yapf](https://github.com/google/yapf), and
   [pycodestyle](https://github.com/PyCQA/pycodestyle).
   of 80 characters per line for code and 72 for docstrings/comments.
* Easy: Analyze a given csv with an argument (python3 plotdicemechanic.py 20170106.csv)
* ~~Medium: Change plotdicemechanic.py from plotly to matplotlib.~~
* ~~Medium: Export a simulation .csv file directly to a graph in .png format~~
* ~~Medium: Output graph of simulation output in .png format instead of html.~~
* Medium: Analyze and plot averages from multiple csv files.

# Experiments

* What are the results when only PC vs PC occurs?

* What are the results when only PC vs NPC occurs?

* What are the results of all players choosing maximum points?

* What are the results of all players choosing minimum points?

* Compare Event 7 resolution methods

# Example score tables

* ~~Medium: Loss table~~
```
      PC    vs PC d4    vs PC d6    vs PC d8    vs PC d10
      d6        3           2           1           1
      d8        5           4           3           1
      d10       7           6           5           4
```
* ~~Medium: Higher point table~~
```
      PC    vs PC d4    vs PC d6    vs PC d8    vs PC d10
      d4        3           4           5           6
      d6        2           3           4           5
      d8        1           2           3           4
      d10       1           1           2           3
```

* Early concept

If you have a higher dice than PC, 1 point.

If you have the same dice as PC, 2 points.

If you have 1 lower dice than PC, 3 points.

If you have 2 lower dice than PC, 4 points.
