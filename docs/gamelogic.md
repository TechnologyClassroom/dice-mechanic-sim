# Game Logic

Game logic for Midnight Riders

Michael McMahon

- Roll twelve sided dice (D12s) to settle any ties throughout the game.

## Start of the game

- Decide number of player characters (PCs)
- For each PC, create two variables to keep track of madness and reputation
  scores (1M, 1R, 2M, 2R, ..., nM, nR).
- Set all M and R variables equal to starting score.

## Event steps for events 1 through 6 (Loop)

- PCs roll off to decide player order. (Skip in simulation)
  - Instead, PC turn order starts with player 1.
- Happening modifier
  - PC rolls a D4 and a D12 to choose a happening.
  - The happening adds a modifier to the round. (Skip in simulation)
- The number of PCs equals the number of scenes that occur for each event.
- Save output scores in CSV format.

## Scene Steps (Loop)

- PC decides to play for Reputation or Madness.
- PC decides to oppose another PC or a non-player character (NPC).
  - If the PC faces an NPC, decide the level of challenge: easy, medium, or hard
- PCs collaboratively tell a story resulting in conflict. (Skip in simulation)
- PCs roll on conflict.
- PCs collaboratively tell the conclusion to the conflict. (Skip in simulation)
- The winning PC gains Reputation or Madness depending on the choice earlier.
- If any PCs' score is less than minimum score, change to minimum score.

## Win conditions and event 7

- Roll twelve sided dice (D12s) to settle ties.
- After event 6, find PC or PCs that have the highest reputation or madness.
- If a PC has the highest reputation and madness, there is no event 7 and that
  PC wins.  If multiple PCs tie for both highest reputation and madness,
  there is no event 7 and they each roll a D12 to see who wins.
- Event 7 (Beta) (Currently in the simulation)
  - The PC with the highest madness defends against the PC with highest rep.
    - D12 + madness vs D12 + reputation
  - When two or more characters have highest madness and/or reputation, roll
- Event 7 (Bracket) (Not currently in the simulation)
  - The PC with the highest madness has become too powerful.  All other PCs
    fight in a single-elimination bracket system to see who will face off
    against the strongest PC.
  - The bracket builds up from the players with the lowest reputation to the
    highest reputation.
  - PCs use the dice tier chart to determine which die they roll.
  - Opposing PCs roll their die and add their reputation.  Highest number
    wins and continues through the bracket.
  - The last two PCs in the bracket may team up.
  - Final Event 7 battle is a best 2 out of 3 with the highest madness
    player against the winner of the bracket.  The madness PC uses the dice
    tier chart to determine which die they roll.
    - Die tier + madness vs Die tier + reputation
  - See [pages 7 and 8 of the first printing](https://github.com/GhostCityGames/Midnight-Riders/releases/download/v1.0/MidnightRiders-GhostCityGames.pdf) for the complete rules.
  - Event 7 edge case: If 2 or more players tie for highest madness, they
    each roll a D12 to settle the tie. The winner of the D12 roll now has the
    highest madness and must be stopped by the winner of the bracket.
- The winner PC tells the tale of how they take control of the land.
