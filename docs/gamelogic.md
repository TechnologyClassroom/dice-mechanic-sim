# gamelogic.md

Game logic for dice-mechanic-simulator

Michael McMahon

## Start of the game

- Decide number of players
- For each player, create two variables (1M, 1R, 2M, 2R, ..., nM, nR).
- Set all M and R variables equal to starting score.

## Event steps (Loop)

- Players roll off to decide player order. (Skip in simulation)
  - Instead, player turn order starts with player 1.
- Happening modifier
  - Player rolls a D4 and a D12 to choose a happening.
  - The happening adds a modifier to the round. (Skip in simulation)
- Player number of scenes occur for each event.
- Save output scores in CSV format.

## Scene Steps (Loop)

- Player decides to play for Reputation or Madness.
- Player decides which opponent to face or NPC.
  - If the player faces an NPC, decide the level of challenge.
- Player tells a story with others resulting in conflict. (Skip in simulation)
- Players roll on conflict.
- The winning Player gains Reputation or Madness.
- If any players' score is less than minimum Score, change to minimum score.

## Win conditions and event 7 (Outdated)

- Find player or players that have max reputation and madness.
- If a player has the highest repuation and madness, there is no event 7.
- Event 7
  - The PC with the highest madness defends against the PC with highest rep.
    - D12+madness vs D12+reputation
  - When two or more characters have highest madness and/or reputation, roll
- D12s to settle ties.
