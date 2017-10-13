# Game balance goals
Goals for the game mechanics to become more fun and balanced:

1) Numbers and dice consistently learning towards higher numbers as the game progresses

2) Close matches

3) High probability of event 7

4) Low probability of getting stuck at the first dice tier

Data analysis can be achieved by watching simulations over time and with data analysis and graphing libraries (numpy and matplotlib).


# Feature requests
- Only load pieces of libraries that are used to speed up processing time
- Proposed changes for dice tiers and points
  - Change point system for PC vs PC based on dice advantage
    - If you have a higher dice than PC, 1 point.
    - If you have the same dice as PC, 2 points.
    - If you have 1 lower dice than PC, 3 points.
    - If you have 2 lower dice than PC, 4 points.
- Output graph of simulation output in .png format in addition to .csv format.
- pep 8


# Experiments

1) What are the results of all players choosing maximum points?

2) What are the results of all players choosing minimum points?

3) New ways of calculating scores (The "underdog" comeback scoring mechanism)

4) What are the results when only PC vs PC occurs?

5) What are the results when only PC vs NPC occurs?

6) Event 7 resolution methods
