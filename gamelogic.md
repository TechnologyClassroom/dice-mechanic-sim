# gamelogic.txt

Game logic for dice-mechanic-simulator

Michael McMahon

# Start of the game
- Decide number of players
- For each player, create two variables (M1, R1, M2, R2, ..., M5, R5).
- Set all M and R variables = 3

# Event steps (Loop)
- Player turn order restarts at player1
- Players roll off to decide who chooses a happening first. (Skip in simulation)
- Player number of happenings occur

# Happening Steps (Loop)
- If any players' score is less than minimum Score, change to minimum score.
- Player rolls a D4 and a D12 to choose a happening. (Skip in simulation)
- Player decides the level of challenge (1, 2, or 3).
- Player decides to fight NPC or PC.
  - If a challenge of 3 is selected, choose between which PC randomly.
- Player decides to play for Reputation or Madness.
- Player tells a story with others resulting in conflict. (Skip in simulation)
- Players roll on conflict.
   If rolling against challenge 1, roll against D4.
   If rolling against challenge 2, roll against D6.
   If rolling against challenge 3, roll against D8 or opposing PC trait die.
- Player gains or loses Reputation or Madness based on win or lose.
- Save output scores in CSV format.

# Win conditions and event 7
- New arrays for reputation and madness using modulo to output even and odd
- Find max value for each array
- Find player or players that have max scores
- Record player or players with highest reputation.
- Record player or players with highest madness.
- if a player has the highest repuation and madness, there is no event 7.

#   Event 7
- The PC with the highest madness defends against the PC with highest rep.
    - D12+madness vs D12+rep


# Feature request
- Only load pieces of libraries that are used to speed up processing time
- Proposed changes for dice tiers and points
  - Change point system for PC vs PC based on dice advantage
    - If you have a higher dice than PC, 1 point.
    - If you have the same dice as PC, 2 points.
    - If you have 1 lower dice than PC, 3 points.
    - If you have 2 lower dice than PC, 4 points.
- Output graph of simulation output in .png format in addition to .csv format.
- pep 8


# Game balance goals
Goals for the game mechanics to become more fun and balanced:

1) Numbers and dice consistently learning towards higher numbers as the game progresses

2) Close matches

3) High probability of event 7

4) Low probability of getting stuck at the first dice tier

Data analysis can be achieved by watching simulations over time and with data analysis and graphing libraries (numpy and matplotlib).




# Experiments

1) What are the results of all players choosing maximum points?

2) What are the results of all players choosing minimum points?

3) New ways of calculating scores (The "underdog" comeback scoring mechanism)

4) What are the results when only PC vs PC occurs?

5) What are the results when only PC vs NPC occurs?

6) Event 7 resolution methods
