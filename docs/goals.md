# Goals & Feature requests

# Game balance goals
Goals for the game mechanics to become more fun and balanced:

1) Numbers and dice consistently learning towards higher numbers as the game progresses

2) Close matches

3) High probability of event 7

4) Low probability of getting stuck at the first dice tier

Data analysis can be achieved by watching simulations over time and with data analysis and graphing libraries (numpy and matplotlib).

# Road map to v1.0:
-Event 7 edge cases need to be addressed

# Feature requests
- Easy: [pep 8 style])(https://www.python.org/dev/peps/pep-0008)
  - [Maximum line length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
  of 80 characters per line for code and 72 for docstrings/comments.
- Easy: Only load pieces of libraries that are used to speed up processing time
- dicemechanicsim.py
  - Easy: Run plotdicemechanic.py at the end of dicemechanicsim.py on the csv file.
  - Medium: Proposed changes for dice tiers and points
    - Change point system for PC vs PC based on dice advantage
      - If you have a higher dice than PC, 1 point.
      - If you have the same dice as PC, 2 points.
      - If you have 1 lower dice than PC, 3 points.
      - If you have 2 lower dice than PC, 4 points.
    - Higher point table
      - PC    vs PC d4    vs PC d6    vs PC d8    vs PC d10
      - d4        3           4           5           6
      - d6        2           3           4           5
      - d8        1           2           3           4
      - d10       1           1           2           3
- plotdicemechanic.py
  - Medium: Change plotdicemechanic.py from plotly to matplotlib.
  - Medium: Output graph of simulation output in .png format instead of html.

# Experiments

1) What are the results of all players choosing maximum points?

2) What are the results of all players choosing minimum points?

3) New ways of calculating scores (The "underdog" comeback scoring mechanism)

4) What are the results when only PC vs PC occurs?

5) What are the results when only PC vs NPC occurs?

6) Event 7 resolution methods
