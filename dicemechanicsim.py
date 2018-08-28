#!/usr/bin/env python
"""dicemechanicsim (DMS) tests game mechanics for the RPG Midnight Riders."""

# dicemechanicsim.py
# Dice Mechanic Simulation v0.98

# Michael McMahon

# DMS can be used to balance dice based RPGs and board games.

# DMS tested with Python 3.5.2, pandas 0.20.3, matplotlib 2.1.0, and Debian 9.

# Run with this command:
#   python dicemechanicsim.py
#
# View help:
#   python dicemechanicsim.py -h
#
# Enable verbose mode:
#   python dicemechanicsim.py -v

# Python 2 Information
# To run dms with python 2, remove, change, comment these three lines:
# Remove "import plotdicemechanic"
# Change this line 'file = open(filename, "w", newline="")  # Python 3'
# to this 'file = open(filename, "wb")  # Python 2'
# Remove "plotdicemechanic.plotaspng(filename)"

# Import libraries
import csv  # Export to csv format
# from csv import writer, writerow  # Export to csv format
from argparse import ArgumentParser  # Add switch arguments for python 2.7&3.2+
from random import randrange  # dice rolls and probability
from time import localtime  # Name output file with timestamp
from time import strftime  # Name output file with timestamp
from plotdicemechanic import plotaspng  # Python 3
from roll import roll

# Variables
# Modify the numbers in this section to experiment with game settings

# Number of Players
N = randrange(3, 6)  # Choose number of players randomly (3-5)
# N = 4  # Static number of players
# Uncomment the line above to assign a specific number of palyers.

# Scenes
H = N * 6  # Scene = Players * Events
# Homebrew: Increase Event number to add more conflicts to simulate
# battles with multiple PCs or extended games.

# Starting Score DEBUG
SS = 0

# Minimum Score DEBUG
MS = 0

#  PC Dice tiers example
#   0      = d4
#   1 -  5 = d6
#   6 - 12 = d8
#  13+     = d10

#  PC Dice tiers variables table
#  TIER0               = d4
#  TIER0 through TIER1 = d6
#  TIER1 through TIER2 = d8
#  TIER2+              = d10

# Dice tier variables DEBUG
TIER0 = 0
TIER1 = 6
TIER2 = 12
# TIER3 = 20
# TIER4 = 30

# PC vs PC point variables table
#  PC    vs PC d4    vs PC d6    vs PC d8    vs PC d10
#  d4     POINTD      POINTC      POINTB      POINTA
#  d6     POINTE      POINTD      POINTC      POINTB
#  d8     POINTF      POINTE      POINTD      POINTC
#  d10    POINTF      POINTF      POINTE      POINTD

# PC vs PC points DEBUG
POINTA = 4
POINTB = 4
POINTC = 4
POINTD = 3
POINTE = 2
POINTF = 1
POINTG = 0

# Penalty for d4 PC vs PC dice
FOURPEN = 2

# PC vs NPC point table
#       vs NPC d4     vs NPC d6    vs NPC d8
# PC     pointO        pointN       pointM

# PC vs NPC points DEBUG
# Difference in PC vs NPC table
NPCPEN = 1

# d4 against d6 has an added penalty to match chart.
D4D6PEN = 1

# Current Relational Point Table
# PC   vsPCd4   vsPCd6   vsPCd8   vsPCd10   vsNPCd4   vsNPCd6   vsNPCd8
# d4     1        1        2        2          1         1         2
# d6     2        3        4        4          1         2         3
# d8     1        2        3        4          0         1         2
# d10    1        1        2        3          0         0         1

# Chance of NPC battles
# NPCGATE1 allows a hard percentage before any opponents are picked.
# NPCGATE2 allows a chance to reroll if an NPC is picked.
NPCGATE1 = 20
NPCGATE2 = 25
# Probability of facing NPC = (gate1/100)+(1-gate1/100)*(1/(N+1))*(gate2/100)
# The resulting probability is listed at the end of each simulation.

# NPCTIERS aids in upcoming addition of AI.
# Each NPC has an appended dice tier in the tiers array.
NPCTIERS = [0, 0, 1, 1, 2, 2]

# argparse module
# argparse adds switches -h, and -v, and --verbose to the script.
PARSER = ArgumentParser(
    description='DMS tests game mechanics for the RPG Midnight Riders.')
PARSER.add_argument('-v', '--verbose',
                    help='Show all information.', action="store_true")
ARGS = PARSER.parse_args()

# Starting game information
if ARGS.verbose:
    print(str(N) + " players and " + str(H) + " scenes.")
    print("Starting SCORE:" + str(SS) + " Minimum SCORE:" + str(MS) + ".")

# csv file output
TIME = strftime("%Y%m%d%H%M%S", localtime())  # Time variable
FILENAME = str(TIME) + '.csv'
print(FILENAME)

# Open new csv file
FILE = open(FILENAME, "w", newline="")  # Python 3
# Choose csv settings as comma, single quote, and only quote nonnumeric data.
WRITER = csv.writer(FILE, delimiter=',', quotechar="'",
                    quoting=csv.QUOTE_NONNUMERIC)

# Build a SCORE array with (2 x the number of players) length filled with SS.
SCORE = []
for x in range(0, N * 2):
    SCORE.append(SS)

# Build a Score Key that will contain cell headers.
SCORE_KEY = []

# Generate column headers for each player.  1R,1M,2R,2M,...,nR,nM
# The header format is player number followed by type of point.
for cell in SCORE:
    if len(SCORE_KEY) % 2 == 0:
        SCORE_KEY.append(str(int(len(SCORE_KEY) / 2) + 1) + "M")
    else:
        SCORE_KEY.append(str(int(len(SCORE_KEY) / 2) + 1) + "R")

# Add an index in column 0 for data analysis
INDEX = "Event"
SCORE_KEY = [INDEX] + SCORE_KEY
INDEX = 0
SCORE = [INDEX] + SCORE
# From Rohit Jain at https://stackoverflow.com/questions/17911091

# CSV header
# Prints a line at the top of the CSV which labels each column.
print(','.join(map(str, SCORE_KEY)))
WRITER.writerow(SCORE_KEY)
# Starting SCOREs
print(','.join(map(str, SCORE)))
WRITER.writerow(SCORE)

# Functions


# Variables are at the top of this script.
def dicetier(level):
    """Find dice tier"""
    if level <= TIER0:
        return 0
    if level <= TIER1:
        return 1
    if level <= TIER2:
        return 2
    if TIER2 < level:
        return 3
    # if level <= TIER4:
    #     return 4
    # if TIER4 < level:
    #     return 5
    print("ERROR: level is not a number!!")
    return None


def pcdice(pcl):
    """Find PC roll"""
    level = SCORE[(2 * pcl) - 1 + rpmd]  # PC level variable
    if level <= TIER0:
        if ARGS.verbose:
            print("Rolling a D4...")
        return roll(4)
    if level <= TIER1:
        if ARGS.verbose:
            print("Rolling a D6...")
        return roll(6)
    if level <= TIER2:
        if ARGS.verbose:
            print("Rolling a D8...")
        return roll(8)
    if TIER2 < level:
        if ARGS.verbose:
            print("Rolling a D10...")
        return roll(10)
    # if level <= TIER4:
    #     if ARGS.verbose:
    #         print("Rolling a D12...")
    #     return roll(12)
    # if TIER4 < level:
    #     if ARGS.verbose:
    #         print("Rolling a D20...")
    #     return roll(20)
    print("ERROR: level is not a number!!")
    return None


def opposingforce():
    """Choose an opponent to battle"""
    # Control the chances of fighting NPCs.
    chance = roll(100)
    if chance < (NPCGATE1 + 1):  # Chance of not facing NPC.
        return 0
    # Pick an opposing player randomly.
    ofo = randrange(0, (N + 1))

    # NPC
    if ofo == 0:
        # Control the chances of fighting NPCs.
        chance = roll(100)
        # Chance of rerolling if NPC is chosen.
        if chance < (NPCGATE2 + 1):
            return 0
        ofo = randrange(1, (N + 1))
        # Check to see if you picked yourself.
        if int(ofo) != int(TURN):
            return ofo
        if ARGS.verbose:
            print("You tried to fight yourself!")
            print("Rerolling for a new opponent...")
        return opposingforce()
    # Check to see if you picked yourself.
    if int(ofo) != int(TURN):
        return ofo
    if ARGS.verbose:
        print("You tried to fight yourself!")
        print("Rerolling for a new opponent...")
    return opposingforce()


# In the event of a tie, both players roll a D12.
def tiebreak():
    """Tie breaker"""
    player1 = roll(12)
    player2 = roll(12)
    if player1 > player2:
        if ARGS.verbose:
            print("Player " + str(TURN) + " wins the tie!")
        return True
    if player1 < player2:
        if ARGS.verbose:
            if opp == 0:
                print("NPC wins the tie!")
            else:
                print("Player " + str(opp) + " wins the tie!")
        return False
    if ARGS.verbose:
        print("Tie again!")
    tiebreak()
    return None


# Game loop plays through 6 events.
# Each loop is one Scene.
for x in range(0, H):
    # Loop Variables
    current = x + 1  # Scene variable

    TURN = ((current - 1) % N) + 1  # Player turn variable

    # Increase event index by one at the beginning of a new event
    if TURN == 1:
        SCORE[0] = SCORE[0] + 1

    if ARGS.verbose:
        # Insert a blank line for new events when in verbose
        if TURN == 1:
            print("")
        print("Current Event: " + str(SCORE[0]))
        print("Current Scene: " + str(current))
        print("Turn: Player " + str(TURN))

    # Rolling for happening modifier (ignored in simulation)
    if TURN == 1:  # Only occurs at the beginning of each Event.
        h1 = roll(4)
        h2 = roll(12)
        if ARGS.verbose:
            print("Happening modifiers: " + str(h1) + " & " + str(h2))

    # Incomplete AI: Use tiers to inform the next three decisions

    # Decide to go for Reputation or Madness
    rpmd = randrange(0, 2)
    if ARGS.verbose:
        if rpmd == 0:
            print("Rolling for Madness!")
        else:
            print("Rolling for Reputation!")

    # Calculate PC dice tier and roll
    opplevel = SCORE[(2 * TURN) - 1 + rpmd]  # opp level variable
    pctier = dicetier(opplevel)
    if ARGS.verbose:
        print("PC dice tier: " + str(pctier))
    pcroll = pcdice(TURN)

    # Choose opponent
    opp = opposingforce()

    # PC opponent level, dicetier, and roll.
    if opp > 0:
        opplevel = SCORE[(2 * opp) - 1 + rpmd]  # opp level variable
        optier = dicetier(opplevel)
        if ARGS.verbose:
            print("PC vs PC")
            print("Player chose to go up against player " + str(opp) + "!")
            print("Opponent dice tier: " + str(pctier))
        oproll = pcdice(opp)

    # NPC opponent
    if opp == 0:
        if ARGS.verbose:
            print("PC vs NPC")

        # Choose NPC difficulty and risk
        # Static choices can be selected for player 1, late game, or all PCs.
        if TURN == 1:  # Experiment with Player 1 static choices
            chlng = roll(3)  # Default action
            # chlng = 3 # Static choice
            # Uncomment the above line to set a static challenge for Player 1.
        elif current > (H / 6) * 3:  # Experiment with late game static choices
            chlng = roll(3)  # Default action
            # chlng = 3 # Static choice
            # Uncomment the above line to set a static challenge for late game.
        else:
            chlng = roll(3)
            # chlng = 3
            # Uncomment the above line to set a static challenge choice.

        if ARGS.verbose:
            print("NPC challenge rating: " + str(chlng))

        # PC vs NPC scoring DEBUG
        # Calculate NPC opponent dicetier and roll
        if chlng == 1:
            oproll = roll(4)
            optier = 0
        elif chlng == 2:
            oproll = roll(6)
            optier = 1
        elif chlng == 3:
            oproll = roll(8)
            optier = 2
        else:
            print("ERROR: chlng is not 1-3!!")

    # Determine dice tier difference.
    delta = pctier - optier

    # PC vs PC scoring
    # Amount of difference sets point difference as challenge value.
    # chlng is short for challenge and how much is at risk.
    # gnlhc is chlng backwards and is how much the Opponent is risking.
    if delta == 0:
        chlng = POINTD
        gnlhc = POINTD
    elif delta == -1:
        chlng = POINTC
        gnlhc = POINTE
    elif delta == -2:
        chlng = POINTB
        gnlhc = POINTF
    elif delta == -3:
        chlng = POINTA
        gnlhc = POINTF
    elif delta == 1:
        chlng = POINTE
        gnlhc = POINTC
    elif delta == 2:
        chlng = POINTF
        gnlhc = POINTB
    elif delta == 3:
        chlng = POINTF
        gnlhc = POINTA
    else:
        print("ERROR: Dice Tier difference is unexpected!!!")

    # Penalty for first tier dice
    if pctier == 0:
        gnlhc = gnlhc - FOURPEN
        if optier == 1:
            chlng = chlng - D4D6PEN
    if optier == 0:
        gnlhc = gnlhc - FOURPEN
        if pctier == 1:
            gnlhc = gnlhc - D4D6PEN

    # Difference in PC vs NPC table
    if opp == 0 and pctier > 0:
        chlng = chlng - NPCPEN

    if ARGS.verbose:
        print("PC rolls " + str(pcroll) + "!")
        print("Opponent rolls " + str(oproll) + "!")

    # Compare rolls and add / remove challenge points.
    if opp == 0:
        if pcroll > oproll:
            if ARGS.verbose:
                print("WIN!")
            SCORE[(2 * TURN) - 1 + rpmd] = SCORE[(2 * TURN) - 1 + rpmd] + chlng
        elif pcroll < oproll:
            if ARGS.verbose:
                print("LOSE!")
            # SCORE[(2 * TURN) - 1 + rpmd] =
            # SCORE[(2 * TURN) - 1 + rpmd] - chlng
            t = 0  # Do nothing machine
        elif pcroll == oproll:
            if ARGS.verbose:
                print("TIE!")
            if tiebreak() is True:
                if ARGS.verbose:
                    print("WIN!")
                SCORE[(2 * TURN) - 1 + rpmd] = SCORE[(2 *
                                                      TURN) - 1 + rpmd] + chlng
            else:
                if ARGS.verbose:
                    print("LOSE!")
                # SCORE[(2 * TURN) - 1 + rpmd] =
                #     SCORE[(2 * TURN) - 1 + rpmd] - chlng
                t = 0  # Do nothing machine
        else:
            print("ERROR: pcroll or oproll is invalid!")
    else:
        if pcroll > oproll:
            if ARGS.verbose:
                print("WIN!")
            SCORE[(2 * TURN) - 1 + rpmd] = SCORE[(2 * TURN) - 1 + rpmd] + chlng
            # SCORE[(2 * opp) - 1 + rpmd] = SCORE[(2 * opp) - 1 + rpmd] - gnlhc
        elif pcroll < oproll:
            if ARGS.verbose:
                print("LOSE!")
            # SCORE[(2 * TURN) - 1 + rpmd] = SCORE[(2 *
            #                                       TURN) - 1 + rpmd] - chlng
            SCORE[(2 * opp) - 1 + rpmd] = SCORE[(2 * opp) - 1 + rpmd] + gnlhc
        elif pcroll == oproll:
            if ARGS.verbose:
                print("TIE!")
            if tiebreak() is True:
                if ARGS.verbose:
                    print("WIN!")
                SCORE[(2 * TURN) - 1 + rpmd] = SCORE[(2 *
                                                      TURN) - 1 + rpmd] + chlng
                # SCORE[(2 * opp) - 1 + rpmd] = SCORE[(2 *
                #                                      opp) - 1 + rpmd] - gnlhc
            else:
                if ARGS.verbose:
                    print("LOSE!")
                # SCORE[(2 *
                #        TURN) - 1 + rpmd] = SCORE[(2 *
                #                                   TURN) - 1 + rpmd] - chlng
                SCORE[(2 * opp) - 1 + rpmd] = SCORE[(2 *
                                                     opp) - 1 + rpmd] + gnlhc
        else:
            print("ERROR: pcroll or oproll is invalid!")

    # Results

    # If a SCORE value is below zero at the end of a scene, bump up to zero.
    for checkms in SCORE[1:]:
        if checkms < 0:
            SCORE[SCORE.index(checkms)] = MS

    # AI: Calculate dice tiers for all stats and overwrite list
    tiers = []
    for SCORES in SCORE[1:]:
        tiers.append(dicetier(SCORES))
    tiers = tiers + NPCTIERS  # [0,0,1,1,2,2]
    # if ARGS.verbose:
    #     print("Dice tiers for AI")
    #     print(','.join(map(str, tiers)))

    # Score after each Scene
    if ARGS.verbose:
        print("Scene scores")
        print(','.join(map(str, SCORE)))

    # Score after each event
    if TURN == N:
        if ARGS.verbose:
            print("Final event scores:")
        print(','.join(map(str, SCORE)))
        WRITER.writerow(SCORE)

# Events 1-6 are complete.
# Find WINner or play event 7

# Calculate max Repuation and Madness after 6 events

# Make new arrays for Madness and Reputation
EV6MAD = SCORE[1::2]
EV6REP = SCORE[2::2]

if ARGS.verbose:
    print("Event 6 Madness: " + str(EV6MAD))
    print("Event 6 Reputation: " + str(EV6REP))

MEV6MAD = max(EV6MAD)
MEV6REP = max(EV6REP)

print("Highest Madness:," + str(MEV6MAD))
print("Highest Reputation:," + str(MEV6REP))

# Find player or players that have max SCOREs
TOPMAD = []
TOPREP = []

# Record player or players with highest madness.
for i, j in enumerate(EV6MAD):
    if j == MEV6MAD:
        TOPMAD.append(i + 1)

# Record player or players with highest reputation.
for i, j in enumerate(EV6REP):
    if j == MEV6REP:
        TOPREP.append(i + 1)

print("Player(s) with highest Madness:," + str(TOPMAD))
print("Player(s) with highest Reputation:," + str(TOPREP))

# if a player has the highest madness and reputation, there is no event 7.
if len(TOPREP) == len(TOPMAD) == 1 and TOPREP == TOPMAD:
    WIN = TOPMAD[0]
# Event 7
elif len(TOPMAD) == 1 and len(TOPREP) == 1:
    # The player with the highest madness rolls a D12 + madness
    EV7MAD = roll(12) + MEV6MAD
    # The player with the highest reputation rolls a D12 + reputation
    EV7REP = roll(12) + MEV6REP

    # Winner takes all
    if EV7MAD > EV7REP:
        if ARGS.verbose:
            print("WIN!")
        WIN = TOPMAD[0]
    elif EV7MAD < EV7REP:
        if ARGS.verbose:
            print("LOSE!")
        WIN = TOPREP[0]
    elif EV7MAD == EV7REP:
        if ARGS.verbose:
            print("TIE!")
        if tiebreak() is True:
            if ARGS.verbose:
                print("WIN!")
            WIN = TOPMAD[0]
        else:
            if ARGS.verbose:
                print("LOSE!")
            WIN = TOPREP[0]
else:
    WIN = "EVENT 7 EDGE CASE!"

# Report if there is a winner
print("Winner:," + str(WIN))

# (Optional) Print the SCORE table

# Probability of facing NPCs
# Probability of facing NPC = (gate1/100)+(1-gate1/100)*(1/(N+1))*(gate2/100)
PROB = round(100 * ((NPCGATE1 / 100) + (1 - NPCGATE1 / 100) * (1 / (N + 1)) *
                    (NPCGATE2 / 100)), 1)
print("Probability of choosing NPC as a random opponent is " +
      str(PROB) + "%.")

# Close csv file lock
FILE.close()

# (Optional) run python script on csv to graph results.
plotaspng(FILENAME)  # Python 3
