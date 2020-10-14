# Goals & Feature requests

## Game balance goals

Goals for the game mechanics to become more fun and balanced:

1) Numbers and dice should consistently increase as the game progresses
2) The game should end in close matches
3) High probability of event 7
4) Low probability of getting stuck at the first dice tier
5) Low probability of leaving a player left behind

Data analysis can be achieved by watching simulations over time or with data
analysis.

## Experiments

- What are the results when only PC vs PC occurs?
- What are the results when only PC vs NPC occurs?
- What are the results of all players choosing maximum points?
- What are the results of all players choosing minimum points?
- Compare Event 7 resolution methods

## builddatapack.sh Feature requests

- [ ] Medium: Convert to pure python without gpicview or zip dependency.
  - [ ] Replace zip with zipfile module

## dicemechanicsim.py Feature requests

- [ ] Easy: create setup.py.
- [ ] Easy: Translate this document into github issues.
- [ ] Easy: Change variable numbers to improve
  [game balance](https://github.com/TechnologyClassroom/dice-mechanic-sim/blob/master/docs/goals.md#game-balance-goals)
  and propose changes for dice tiers and points.
- [ ] Medium: [Create strategies for the players (Fake AI)](https://github.com/TechnologyClassroom/dice-mechanic-sim/issues/5)
  - [ ] Turn delta section into a function.
  - [ ] A new array will be created at the beginning of each scene that would
    calculate the possible scores for each conflict.
  - [ ] Applying strategy involves the PC choosing the opponent that yields a
    balance of the highests points with lowest risk.
- [ ] Easy: [Only load pieces of libraries that are used](https://github.com/TechnologyClassroom/dice-mechanic-sim/issues/4)
- [ ] Medium: Create a player generator to add flavor from MR using classes
- [ ] Medium: [Event 7 needs to match first printing.](https://github.com/TechnologyClassroom/dice-mechanic-sim/issues/6)
  - [ ] Bracket system that pits all runner up PCs against each other to decide
    who faces the player with the highest madness.
  - [ ] The last two players in the bracket may team up.
  - [ ] Final Event 7 battle is a best 2 out of 3 with the highest madness
    player against the winner of the bracket.
  - [ ] D12 will settle ties during event 7.
  - [ ] Event 7 edge case: If 2 or more players tie for highest madness, roll
    off with D12.  The winner of all D12 rolls has the highest madness and
    must be stopped by the winner of the bracket.
  - [ ] Event 7 edge case: What happens when two players tie for highest
    madness and repuatation?
- [ ] Medium: [Apply happening modifiers to the simulation.](https://github.com/TechnologyClassroom/dice-mechanic-sim/issues/7)
  - [ ] Medium: Fight a random number of opponents in special happenings.
- [ ] Advanced: Include CI workflow with tox.ini.
- [ ] Advanced: Add an option for interactive play.

## Data Analysis Feature requests

- [ ] Medium: [Analyse statistics from multiple csv files.](https://github.com/TechnologyClassroom/dice-mechanic-sim/issues/12)
- [ ] Advanced: Create a secondary system that analyzes the output and changes.
  the variables in dicemechanicsim.py autonomously.
- [ ] Advanced: Update code to work with the latest pandas.

## roll Feature requests

- [ ] Advanced: Add to pip.

## Documentation Feature requests

- [ ] Medium: docs/gamelogic Event 7 needs an update to the bracket system from
  the first edition of Midnight Riders.
- [ ] Update the doc folder to sphinx-doc style documenation.

## Testing Feature requests
- [ ] Test changes to `setuptoxtestenvironment.sh`.
- [ ] Add alternative pip installation method to `setuptoxtestenvironment.sh`.
- [ ] Easy-Advanced: Write py.test tests for full coverage.
- [ ] Easy: Create test_dicemechanicsim.py.
- [ ] Easy: Create test_plotdicemechanic.py.
- [ ] Easy: Create test_plotcsv.py.
- [ ] Medium: Configure dependencies so output from numpy is not seen.
- [ ] Easy: Add travis-ci to github.
- [ ] Easy: Add CI to gitlab.
