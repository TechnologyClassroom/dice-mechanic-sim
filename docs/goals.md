# Goals & Feature requests

# Game balance goals
Goals for the game mechanics to become more fun and balanced:

1) Numbers and dice should consistently increase as the game progresses

2) The game should end in close matches

3) High probability of event 7

4) Low probability of getting stuck at the first dice tier

5) Low probability of leaving a player left behind

Data analysis can be achieved by watching simulations over time or with data
analysis.


# builddatapack.sh Feature requests
* Medium: Convert to pure python without gpicview dependency.
* Medium: Before zip, combine event 6 from data sets into database and graph.

# dicemechanicsim.py Feature requests
* Easy: Change variable H to S.
* Easy: Separate roll function into separate roll.py module.
* Medium: Fake AI that makes better decisions than random
  * ~~A new array could be created at the end of each conflict filled with each
  score's dice tier.~~
  * Turn delta section into a function.
  * A new array will be created at the beginning of each scene that would
  calculate the possible scores for each conflict.
  * Applying strategy involves the PC choosing the opponent that yields a
  balance of the highests points with lowest risk.
* Easy: Only load pieces of libraries that are used to speed up processing
time.
* Medium: Update Event 7
  * ~~Check if there is a winner before event 7.~~
  * Bracket system that pits all runner up PCs against each other to decide
  who faces the player with the highest madness.
  * The last two players in the bracket may team up.
  * Final Event 7 battle is a best 2 out of 3 with the highest madness
  player against the winner of the bracket.
  * D12 will settle ties during event 7.
  * Event 7 edge case: If 2 or more players tie for highest madness, roll
  off with D12.  The winner of all D12 rolls has the highest madness and
  must be stopped by the winner of the bracket.
  * Event 7 edge case: What happens when two players tie for highest
  madness and repuatation?
* Medium: Fight a random number of opponents in special happenings
* Easy: Propose changes for dice tiers and points
* Easy: Change code to [pep 8 style](https://www.python.org/dev/peps/pep-0008)
  * [Maximum line length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
  of 80 characters per line for code and 72 for docstrings/comments.
  * A few automatic code analyzers are
  [autopep8](https://github.com/hhatto/autopep8),
  [yapf](https://github.com/google/yapf), and
  [pycodestyle](https://github.com/PyCQA/pycodestyle).
* ~~Easy: Run plotdicemechanic.py at the end of dicemechanicsim.py.~~
* See tables section below
  * ~~Change point system for PC vs PC based on dice advantage~~
  * ~~Medium: Relational NPC scoring with one point less than PC table scores~~
  * ~~Medium: Loss table~~
  * ~~Medium: Higher point table~~

# plotdicemechanic.py Feature requests
* Medium: Analyze and plot averages from multiple csv files.
* Advanced: Create a secondary system that analyzes the data and changes the
variables in dicemechanicsim.py autonomously.
* Easy: Change code to [pep 8 style](https://www.python.org/dev/peps/pep-0008)
  * [Maximum line length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
  of 80 characters per line for code and 72 for docstrings/comments.
  * A few automatic code analyzers are
  [autopep8](https://github.com/hhatto/autopep8),
  [yapf](https://github.com/google/yapf), and
  [pycodestyle](https://github.com/PyCQA/pycodestyle).
* ~~Easy: Analyze a given csv with an argument (python3 plotdicemechanic.py 20170106.csv)~~
* ~~Medium: Change plotdicemechanic.py from plotly to matplotlib.~~
* ~~Medium: Export a simulation .csv file directly to a graph in .png format~~
* ~~Medium: Output graph of simulation output in .png format instead of html.~~

# Experiments

* What are the results when only PC vs PC occurs?

* What are the results when only PC vs NPC occurs?

* What are the results of all players choosing maximum points?

* What are the results of all players choosing minimum points?

* Compare Event 7 resolution methods

# Example score tables

* ~~Relational Point Chart~~
```
PC    vsPCd4    vsPCd6    vsPCd8    vsPCd10    vsNPCd4    vsNPCd6    vsNPCd8
d4      1         1         2         2           1          1          2
d6      2         3         4         4           1          2          3
d8      1         2         3         4           0          1          2
d10     1         1         2         3           0          0          1
```
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
* ~~Early concept~~
  * If you have a higher dice than PC, 1 point.
  * If you have the same dice as PC, 2 points.
  * If you have 1 lower dice than PC, 3 points.
  * If you have 2 lower dice than PC, 4 points.
