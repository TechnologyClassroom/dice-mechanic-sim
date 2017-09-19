# dicemechanicsim.py
# Dice Mechanic Simulation v0.94

# Michael McMahon

# DMS tests game mechanics for the RPG Midnight Riders.
# This script can be used to balance dice based RPGs and board games.

# No AI is present.  All decisions are made randomly.
# Static choices can be selected for player 1.

# Tested with python versions 2.7.12 and 3.5.2.

# Run with this command:
#   python dicemechanicsim.py
#
# View help:
#   python dicemechanicsim.py -h
#
# Enable verbose mode:
#   python dicemechanicsim.py -v


# Import libraries
from random import randrange # dice rolls and probability
import argparse # Add switch arguments for python v2.7 and v3.2+
import csv # Export to csv
#from csv import writer, writerow
from time import strftime, localtime
#import matplotlib.pyplot as plt


# Variables
N = randrange(3,6) # Choose number of players randomly (3-5)
N = 4 # Static number of players
# Comment the above line to player a random game.

H = N * 6 # Happenings = Players * Events

#print(str(N) + " players and " + str(H) + " happenings.") # Debug

SS = 3 # Starting Score

MS = 3 # Minimum Score

#print("Starting score:" + str(SS) + " Minimum score:" + str(MS) + ".") # Debug


# argparse
parser = argparse.ArgumentParser(description='DMS tests game mechanics for the RPG Midnight Riders.')
parser.add_argument('-v', '--verbose', help='Show all information.', action="store_true")
args = parser.parse_args()


# csv file output
time = strftime("%Y%m%d%H%M%S", localtime()) # Time variable
filename = str(time) + '.csv'
print(filename)
file = open(filename, "wb")
writer = csv.writer(file, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)


# Build a score array with (2 x the number of players) length filled with SS.
score = []

for x in range(0, N*2):
  score.append(SS)


# Build a Score Key that will contain cell headers.
score_key = []

for cell in score:
  if len(score_key) % 2 == 0:
    score_key.append("R" + str((len(score_key)/2)+1))
  else:
    score_key.append("M" + str((len(score_key)/2)+1))

print(','.join(map(str, score_key))) # CSV header
writer.writerow(score_key)
print(','.join(map(str, score))) # Starting scores
writer.writerow(score)

# Functions

# Die roll functions
def roll(diefaces):
  return randrange(1, int(diefaces+1))


# Choose an opponent PC to battle 
def OpposingForce():
  of = randrange(0, (N+1) )
  # Change above from 0 to 1, to remove NPC from challenge 3.

  if int(of) == 0:
    # Fighting a strong NPC is rare to motivate mutiplayer experience.
    chance = roll(4)
    if chance < 2:
      return of
    else:
      return OpposingForce()
  # Do not pick yourself
  elif int(of) != int(turn):
    return of
  else:
    return OpposingForce() 


#  Dice chart
#   1 -  6 = d6
#   7 - 24 = d8
#  25+     = d10
# Problem: No one gets to roll a d10 ever.

#  Dice chart
#   1 -  6 = d6
#   7 - 13 = d8
#  14+     = d10

def pcdice(pc):
  level = score[ (2 * pc) - 2 + rpmd ] # PC level variable
  if level <= 6:
    if args.verbose:
      print("Rolling a D6...") # Debug
    return roll(6)
  elif 6 < level <= 13:
    if args.verbose:
      print("Rolling a D8...") # Debug
    return roll(8)
  elif 13 < level:
    if args.verbose:
      print("Rolling a D10...") # Debug
    return roll(10)
  #elif 30 < level <= 35:
  #  if args.verbose:
  #    print("Rolling a D12...") # Debug
  #  return roll(12)
  #elif 35 < level:
  #  if args.verbose:
  #    print("Rolling a D20...") # Debug
  #  return roll(20)
  else:
    return "ERROR: level is not a number!!"


# Tie breaker
# In the event of a tie, both players roll a D12.
def tiebreak():
  player1 = roll(12)
  player2 = roll(12)
  if player1 > player2:
    return True
  elif player1 < player2:
    return False
  else:
    tiebreak()


# Game loop plays through 6 events
for x in range(0, H): # Run a full game.
#for x in range (0, H / 6 ): # Only run one event for debug purposes.
# Choose only one of the two lines above, but not both.
  # Loop Variables
  current = x+1 # Happening variable

  turn = ((current-1) % N)+1 # Player turn variable

  opp = 0 # Reset opponent variable.  0=NPC


  # Every new Event gets a blank line
  if args.verbose and turn == 1:
    print("") # Debug

  if args.verbose:
    print("Current happening: " + str(current)) # Debug
    print("Turn: Player " + str(turn)) # Debug


  # If a score value is below the minimum score, bump up to minimum.
  for checkms in score:
    if checkms < MS:
      score[score.index(checkms)] = MS


  # Rolling for happening modifier (ignored in simulation)
  h1 = roll(4)
  h2 = roll(12)
  if args.verbose:
    print("Happening modifiers (Ignored): " + str(h1) + " & " + str(h2)) # Debug

  # Decide amount of difficulty and risk
  if turn == 1: # Experiment with static challenge choices
    chlng = randrange(1,4) # Default action
    if current > (H/6)*3: # Experiment with static choices based on progress.
      chlng = randrange(1,4) # Default action
      #chlng = 3 # Static choice
      # Comment the above line to run a standard simulation.
    #chlng = 3 # Static choice
    # Comment the above line to run a standard simulation.
  else:
    chlng = randrange(1,4)
    chlng = 3
  if args.verbose:
    print("Challenge rating: " + str(chlng)) # Debug


  # Choose opposing PC
  if chlng == 3:
    opp = OpposingForce()
    if args.verbose:
      print("Opponent is player " + str(opp)) # Debug


  # Decide to go for Reputation or Madness
  rpmd = randrange(0,2)
  if args.verbose:
    if rpmd == 0: # Debug
      print("Rolling for Reputation!") # Debug
    else: # Debug
      print("Rolling for Madness!") # Debug


  # Calculate PC dice class and roll
  pcroll = pcdice(turn)
  if args.verbose:
    print("PC rolls " + str(pcroll)) # Debug


  # Calculate opposing dice class and roll
  if chlng == 1:
    oproll = roll(4)
  elif chlng == 2:
    oproll = roll(6)
  elif chlng == 3:
    if opp == 0:
      oproll = roll(8)
    else:
      oproll = pcdice(opp)
  else:
    print("ERROR: chlng is not 1-3!!")

  if args.verbose:
    print("Opponent rolls " + str(oproll)) # Debug


  # Compare rolls and add / remove challenge points.
  if opp == 0:
    if args.verbose:
      print("PC vs NPC") # Debug
    if pcroll > oproll:
      if args.verbose:
        print("WIN!") # Debug
      score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] + chlng
    elif pcroll < oproll:
      if args.verbose:
        print("LOSE!") # Debug
      score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] - chlng
    elif pcroll == oproll:
      if args.verbose:
        print("TIE!") # Debug
      if tiebreak() == True:
        if args.verbose:
          print("WIN!") # Debug
        score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] + chlng
      else:
        if args.verbose:
          print("LOSE!") # Debug
        score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] - chlng
    else:
      print("ERROR: pcroll or oproll is invalid!")
  else:
    if args.verbose:
      print("PC vs PC") # Debug
    if pcroll > oproll:
      if args.verbose:
        print("WIN!") # Debug
      score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] + chlng
      score[ (2 * opp) - 2 + rpmd ] = score[ (2 * opp) - 2 + rpmd ] - chlng
    elif pcroll < oproll:
      if args.verbose:
        print("LOSE!") # Debug
      score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] - chlng
      score[ (2 * opp) - 2 + rpmd ] = score[ (2 * opp) - 2 + rpmd ] + chlng
    elif pcroll == oproll:
      if args.verbose:
        print("TIE!") # Debug
      if tiebreak() == True:
        if args.verbose:
          print("WIN!") # Debug
        score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] + chlng
        score[ (2 * opp) - 2 + rpmd ] = score[ (2 * opp) - 2 + rpmd ] - chlng
      else:
        if args.verbose:
          print("LOSE!") # Debug
        score[ (2 * turn) - 2 + rpmd ] = score[ (2 * turn) - 2 + rpmd ] - chlng
        score[ (2 * opp) - 2 + rpmd ] = score[ (2 * opp) - 2 + rpmd ] + chlng
    else:
      print("ERROR: pcroll or oproll is invalid!")


  # Results

  # score after each happening
  if args.verbose:
    print(','.join(map(str, score))) # Debug

  # score after each event
  if turn == N:
    if args.verbose:
      print("Final event scores:") # Debug
    print(','.join(map(str, score)))
    writer.writerow(score)


# Events 1-6 are complete.
# Find winner or play event 7

# Calculate max Repuation and Madness after 6 events

# Make new arrays for Reputation and Madness
ev6rep = score[::2]
ev6mad = score[1::2]

if args.verbose:
  print("Event 6 Reputation: " + str(ev6rep)) # Debug
  print("Event 6 Madness: " + str(ev6mad)) # Debug

mev6rep = max(ev6rep)
mev6mad = max(ev6mad)

print("Highest Reputation:," + str(mev6rep)) # Debug
print("Highest Madness:," + str(mev6mad)) # Debug

# Find player or players that have max scores
toprep = []
topmad = []

# Record player or players with highest reputation.
for i, j in enumerate(ev6rep):
  if j == mev6rep:
    toprep.append(i+1)

# Record player or players with highest madness.
for i, j in enumerate(ev6mad):
  if j == mev6mad:
    topmad.append(i+1)

print("Player(s) with highest Reputation:," + str(toprep)) # Debug
print("Player(s) with highest Madness:," + str(topmad)) # Debug

# if a player has the highest repuation and madness, there is no event 7.
if len(toprep) == len(topmad) == 1 and toprep == topmad:
  win = topmad[0]
# Event 7
elif len(topmad) == 1 and len(toprep) == 1:
  # The player with the highest madness rolls a D12 + madness
  ev7mad = roll(12) + mev6mad
  # The player with the highest reputation rolls a D12 + reputation
  ev7rep = roll(12) + mev6rep

  # Winner takes all
  if ev7mad > ev7rep:
    if args.verbose:
      print("WIN!") # Debug
    win = topmad[0]
  elif ev7mad < ev7rep:
    if args.verbose:
      print("LOSE!") # Debug
    win = toprep[0]
  elif ev7mad == ev7rep:
    if args.verbose:
      print("TIE!") # Debug
    if tiebreak() == True:
      if args.verbose:
        print("WIN!") # Debug 
      win = topmad[0]
    else:
      if args.verbose:
        print("LOSE!") # Debug
      win = toprep[0]
else:
  win = "EVENT 7 EDGE CASE!"

# Report if there is a winner
print("Winner:," + str(win))


# Close csv file lock
file.close()


# Game logic

# Start of the game
#
# Decide number of players
# For each player, create two variables (M1, R1, M2, R2, ..., M5, R5).
# Set all M and R variables = 3

# Event steps (Loop)
#
# Player turn order restarts at player1
# Players roll off to decide who chooses a happening first. (Skip in simulation)
# Player number of happenings occur

# Happening Steps (Loop)
#
# If any players' score is less than minimum Score, change to minimum score.
# Player rolls a D4 and a D12 to choose a happening. (Skip in simulation)
# Player decides the level of challenge (1, 2, or 3).
# Player decides to fight NPC or PC.
#   If a challenge of 3 is selected, choose between which PC randomly.
# Player decides to play for Reputation or Madness.
# Player tells a story with others resulting in conflict. (Skip in simulation)
# Players roll on conflict.
#   If rolling against challenge 1, roll against D4.
#   If rolling against challenge 2, roll against D6.
#   If rolling against challenge 3, roll against D8 or opposing PC trait die.
# Player gains or loses Reputation or Madness based on win or lose.
# Save output scores in CSV format.

# Win conditions and event 7
#
# New arrays for reputation and madness using modulo to output even and odd
# Find max value for each array
# Find player or players that have max scores
# Record player or players with highest reputation.
# Record player or players with highest madness.
# if a player has the highest repuation and madness, there is no event 7.
#   Event 7
#   The PC with the highest madness defends against the PC with highest rep.
#     D12+madness vs D12+rep

# Feature request
# 
# Refactor libraries for only what I need.
#   sed -i 's/randrange/randrange/g' dicemechanicsim.py
#
# Proposed changes for dice tiers and points
#   Change point system for PC vs PC based on dice advantage
#     If you have a higher dice than PC, 1 point.
#     If you have the same dice as PC, 2 points.
#     If you have 1 lower dice than PC, 3 points.
#     If you have 2 lower dice than PC, 4 points.

# Game balance goals
#
# Numbers and dice consistently leaning towards higher numbers
# https://www.zonebourse.com/zbcache/charts/ObjectChart.aspx?Name=28607554&Type=Custom&Intraday=1&Width=336&Height=360&Cycle=DAY1&Duration=4&Render=Candle&ShowCopyright=2&ShowName=0&Company=4Traders_us
#
# Close matches
#
# High probability of event 7
#
# Unlikelihood of getting stuck at rolling a D6 forever

# Experiments
#
# What are the results of all players chosing maximum points.
#
# How to do make sense of the data
#
# Increase PC vs PC and see how it affects scores
#
# 
#

# Change log 0.95:
# -Ouput to a .csv file in native python
# -Static options for number of player and individual player choice has been
# -Explicit comments have been added

# Road map to v1.0:
# -Event 7 edge cases need to be addressed
