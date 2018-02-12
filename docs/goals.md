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
* Medium: Convert to pure python without gpicview or zip dependency.
  * Replace zip with zipfile module

# dicemechanicsim.py Feature requests
* Easy: Change variable H to S.
* Easy: Add demo using [asciinema](https://asciinema.org/)
* Medium: Change variable numbers to improve 
[game balance](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md#game-balance-goals).
* Medium: Fake AI that makes better decisions than random
  * Turn delta section into a function.
  * A new array will be created at the beginning of each scene that would
    calculate the possible scores for each conflict.
  * Applying strategy involves the PC choosing the opponent that yields a
    balance of the highests points with lowest risk.
* Easy: Only load pieces of libraries that are used to speed up processing
  time.
* Medium: Update Event 7 to match first printing
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
* Medium: Apply happening modifiers to the simulation.
  * Medium: Fight a random number of opponents in special happenings
* Easy: Propose changes for dice tiers and points
* Advanced: Include CI workflow with tox.ini
* Advanced: Add an option for interactive play.

# Data Analysis Feature requests
* Easy: Update example picture to match the new 1M, 1R header format.
* Medium: Analyze and plot averages from multiple csv files by combining event
  6 from all data sets.
* Easy: Run simple statistics of each simulation including:
  * Average score
  * Variance
  * Standard Deviation
* Advanced: Create a secondary system that analyzes the output and changes the
  variables in dicemechanicsim.py autonomously.
* Move all datapacks to a different repository to lower repository size.

# Experiments

* What are the results when only PC vs PC occurs?
* What are the results when only PC vs NPC occurs?
* What are the results of all players choosing maximum points?
* What are the results of all players choosing minimum points?
* Compare Event 7 resolution methods
