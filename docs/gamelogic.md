# gamelogic.txt

Game logic for dice-mechanic-simulator

Michael McMahon

# Start of the game
- Decide number of players
- For each player, create two variables (M1, R1, M2, R2, ..., MN, RN).
- Set all M and R variables = 3

# Event steps (Loop)
- Players roll off to decide who chooses a happening first. (Skip in simulation)
  - Instead, player turn order starts with player 1.
- Player number of happenings occur for each event.

# Happening Steps (Loop)
- Player rolls a D4 and a D12 to choose a happening.
- The happening adds a modifier to the round. (Skip in simulation)
- Player decides to play for Reputation or Madness.
- Player decides which opponent to face or NPC.
- If the player faces an NPC, decide the level of challenge.
- Player tells a story with others resulting in conflict. (Skip in simulation)
- Players roll on conflict.
- Player gains or loses Reputation or Madness based on win or lose.
- If any players' score is less than minimum Score, change to minimum score.
- Save output scores in CSV format.

# Win conditions and event 7
- Find player or players that have max reputation and madness.
- If a player has the highest repuation and madness, there is no event 7.
- Event 7
  - The PC with the highest madness defends against the PC with highest rep.
    - D12+madness vs D12+reputation
  - When two or more characters have highest madness and/or reputation, roll
D12s to settle ties.

