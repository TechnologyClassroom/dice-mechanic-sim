# dicemechanicsim.py
# Dice Mechanic Simulation v0.97

# Michael McMahon

# DMS tests game mechanics for the RPG Midnight Riders.
# This script can be used to balance dice based RPGs and board games.


# Tested with Python v3.5.2, pandas v0.20.3, matplotlib v2.1.0, and Debian v9.2.

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
# Change this line "file = open(filename, "w", newline="")  # Python 3"
# to this "file = open(filename, "wb")  # Python 2"
# Remove "plotdicemechanic.plotaspng(filename)"




# Import libraries
from random import randrange  # dice rolls and probability
import argparse  # Add switch arguments for python v2.7 and v3.2+
import csv  # Export to csv format
#from csv import writer, writerow  # Export to csv format
from time import strftime, localtime  # Name output file with timestamp
import plotdicemechanic  # Python 3




# Variables
# Modify the numbers in this section to experiment with game settings

# Number of Players
N = randrange(3, 6)  # Choose number of players randomly (3-5)
# N = 4  # Static number of players
# Uncomment the line above to assign a specific number of palyers.

# Scenes
H = N * 8  # Scene = Players * Events
# Increase Event number to add more conflicts to compensate for multiple player battles.

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
#  tier0         = d4
#  tier0 - tier1 = d6
#  tier1 - tier2 = d8
#  tier2+        = d10

# Dice tier variables DEBUG
tier0 = 0
tier1 = 6
tier2 = 12
#tier3 = 20
#tier4 = 30

# PC vs PC point variables table
#  PC    vs PC d4    vs PC d6    vs PC d8    vs PC d10
#  d4     pointD      pointC      pointB      pointA
#  d6     pointE      pointD      pointC      pointB
#  d8     pointF      pointE      pointD      pointC
#  d10    pointF      pointF      pointE      pointD

# PC vs PC points DEBUG
pointA = 4
pointB = 4
pointC = 4
pointD = 3
pointE = 2
pointF = 1
pointG = 0

# Penalty for d4 PC vs PC dice
fourpen = 2

# PC vs NPC point table
#       vs NPC d4     vs NPC d6    vs NPC d8
# PC     pointO        pointN       pointM

# PC vs NPC points DEBUG
# Difference in PC vs NPC table
npcpen = 1

# Current Relational Point Table
# PC   vsPCd4   vsPCd6   vsPCd8   vsPCd10   vsNPCd4   vsNPCd6   vsNPCd8
# d4     1        1        2        2          1         1         2
# d6     2        3        4        4          1         2         3
# d8     1        2        3        4          0         1         2
# d10    1        1        2        3          0         0         1




# argparse module
# argparse adds switches -h, and -v, and --verbose to the script.
parser = argparse.ArgumentParser(
    description='DMS tests game mechanics for the RPG Midnight Riders.')
parser.add_argument('-v', '--verbose',
                    help='Show all information.', action="store_true")
args = parser.parse_args()

# Starting game information
if args.verbose:
    print(str(N) + " players and " + str(H) + " happenings.")
    print("Starting score:" + str(SS) + " Minimum score:" + str(MS) + ".")

# csv file output
time = strftime("%Y%m%d%H%M%S", localtime())  # Time variable
filename = str(time) + '.csv'
print(filename)

# Open new csv file
file = open(filename, "w", newline="")  # Python 3
# Choose csv settings as comma, single quote, and only quote nonnumeric data.
writer = csv.writer(file, delimiter=',', quotechar="'",
                    quoting=csv.QUOTE_NONNUMERIC)

# Build a score array with (2 x the number of players) length filled with SS.
score = []
for x in range(0, N * 2):
    score.append(SS)

# Build a Score Key that will contain cell headers.
score_key = []

# Generate column headers for each player.  R1,M1,R2,M2,...,RN,MN
for cell in score:
    if len(score_key) % 2 == 0:
        score_key.append("R" + str(int(len(score_key) / 2) + 1))
    else:
        score_key.append("M" + str(int(len(score_key) / 2) + 1))

# Add an index in column 0 for data analysis
index = "Event"
score_key = [index] + score_key
index = 0
score = [index] + score
# From Rohit Jain at https://stackoverflow.com/questions/17911091/append-integer-to-beginning-of-list-in-python

# CSV header
# Prints a line at the top of the CSV which labels each column.
print(','.join(map(str, score_key)))
writer.writerow(score_key)
# Starting scores
print(','.join(map(str, score)))
writer.writerow(score)




# Functions

# Die roll function
# This function rolls polyhedral dice.  Example: To roll a d8, use roll(8).
def roll(diefaces):
    return randrange(1, int(diefaces + 1))


# Find dice tier
# Variables are at the top of this script.
def dicetier(level):
    if level <= tier0:
        return 0
    elif tier0 < level <= tier1:
        return 1
    elif tier1 < level <= tier2:
        return 2
    elif tier2 < level:
        return 3
    elif tier3 < level <= tier4:
        return 4
    # elif tier4 < level:
    #     return 5
    else:
        return "ERROR: level is not a number!!"


# Find PC roll
def pcdice(pc):
    level = score[(2 * pc) - 1 + rpmd]  # PC level variable
    if level <= tier0:
        if args.verbose:
            print("Rolling a D4...")
        return roll(4)
    elif tier0 < level <= tier1:
        if args.verbose:
            print("Rolling a D6...")
        return roll(6)
    elif tier1 < level <= tier2:
        if args.verbose:
            print("Rolling a D8...")
        return roll(8)
    elif tier2 < level:
        if args.verbose:
            print("Rolling a D10...")
        return roll(10)
    # elif tier3 < level <= tier4:
    #     if args.verbose:
    #         print("Rolling a D12...")
    #     return roll(12)
    # elif tier4 < level:
    #     if args.verbose:
    #         print("Rolling a D20...")
    #     return roll(20)
    else:
        return "ERROR: level is not a number!!"


# Choose an opponent to battle
def OpposingForce():
    # Control the chances of fighting NPCs.
    chance = roll(100)
    if chance < 26:  # 75% chance of rerolling if NPC is chosen.
    # Change above from 26 to 0, to remove NPC conflicts entirely.
        return 0
    else:
        # Pick an opposing player randomly.
        of = randrange(0, (N + 1))

        # Check to see if you picked yourself.
        if int(of) != int(turn):
            return of
        else:
            if args.verbose:
                print("You tried to fight yourself.  Reroll for a new opponent!")
            return OpposingForce()


# Tie breaker
# In the event of a tie, both players roll a D12.
def tiebreak():
    player1 = roll(12)
    player2 = roll(12)
    if player1 > player2:
        if args.verbose:
            print("Player " + str(turn) + " wins the tie!")
        return True
    elif player1 < player2:
        if args.verbose:
            print("Player " + str(opp) + " wins the tie!")
        return False
    else:
        if args.verbose:
            print("Tie again!")
        tiebreak()




# Game loop plays through 6 events.
# Each loop is one happening.
for x in range(0, H):
    # Loop Variables
    current = x + 1  # Happening variable

    turn = ((current - 1) % N) + 1  # Player turn variable

    # Increase event index by one at the beginning of a new event
    if turn == 1:
        score[0] = score[0] + 1

    if args.verbose:
        # Insert a blank line for new events when in verbose
        if turn == 1:
            print("")
        print("Current Event: " + str(score[0]))
        print("Current Happening: " + str(current))
        print("Turn: Player " + str(turn))

    # Rolling for happening modifier (ignored in simulation)
    h1 = roll(4)
    h2 = roll(12)
    if args.verbose:
        print("Happening modifiers: " + str(h1) + " & " + str(h2))

    # Incomplete: Use tiers from AI to decide to inform decisions next three decisions

    # Decide to go for Reputation or Madness
    rpmd = randrange(0, 2)
    if args.verbose:
        if rpmd == 0:
            print("Rolling for Reputation!")
        else:
            print("Rolling for Madness!")

    # Calculate PC dice tier and roll
    level = score[(2 * turn) - 1 + rpmd]  # opp level variable
    pctier = dicetier(level)
    if args.verbose:
        print("PC dice tier: " + str(pctier))
    pcroll = pcdice(turn)

    # Choose opponent
    opp = OpposingForce()

    # PC opponent level, dicetier, and roll.
    if opp > 0:
        level = score[(2 * opp) - 1 + rpmd]  # opp level variable
        optier = dicetier(level)
        if args.verbose:
            print("PC vs PC")
            print("Player chose to go up against player " + str(opp) + "!")
            print("Opponent dice tier: " + str(pctier))
        oproll = pcdice(opp)

    # NPC opponent
    if opp == 0:
        if args.verbose:
            print("PC vs NPC")

        # Choose NPC difficulty and risk
        # Static choices can be selected for player 1, late game, or all players.
        if turn == 1:  # Experiment with Player 1 static choices
            chlng = roll(3)  # Default action
            #chlng = 3 # Static choice
            # Uncomment the above line to set a static challenge choice for Player 1.
        elif current > (H / 6) * 3:  # Experiment with late game static choices
            chlng = roll(3)  # Default action
            #chlng = 3 # Static choice
            # Uncomment the above line to set a static challenge choice for late game.
        else:
            chlng = roll(3)
            #chlng = 3
            # Uncomment the above line to set a static challenge choice.

        if args.verbose:
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
        chlng = pointD
        gnlhc = pointD
    elif delta == -1:
        chlng = pointC
        gnlhc = pointE
    elif delta == -2:
        chlng = pointB
        gnlhc = pointF
    elif delta == -3:
        chlng = pointA
        gnlhc = pointF
    elif delta == 1:
        chlng = pointE
        gnlhc = pointC
    elif delta == 2:
        chlng = pointF
        gnlhc = pointB
    elif delta == 3:
        chlng = pointF
        gnlhc = pointA
    else:
        print("ERROR: Dice Tier difference is unexpected!!!")

    # Penalty for first tier dice
    if pctier == 0:
        gnlhc = gnlhc - fourpen
        if optier == 1:
            chlng = chlng - 1
    if optier == 0:
        gnlhc = gnlhc - fourpen
        if pctier == 1:
            gnlhc = gnlhc - 1

    # Difference in PC vs NPC table
    if opp == 0 and pctier > 0:
        chlng = chlng - npcpen

    if args.verbose:
        print("PC rolls " + str(pcroll) + "!")
        print("Opponent rolls " + str(oproll))

    # Compare rolls and add / remove challenge points.
    if opp == 0:
        if pcroll > oproll:
            if args.verbose:
                print("WIN!")
            score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] + chlng
        elif pcroll < oproll:
            if args.verbose:
                print("LOSE!")
            #score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] - chlng
            print("PC lost against NPC!")
        elif pcroll == oproll:
            if args.verbose:
                print("TIE!")
            if tiebreak() == True:
                if args.verbose:
                    print("WIN!")
                score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] + chlng
            else:
                if args.verbose:
                    print("LOSE!")
                #score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] - chlng
                print("PC lost against NPC!")
        else:
            print("ERROR: pcroll or oproll is invalid!")
    else:
        if pcroll > oproll:
            if args.verbose:
                print("WIN!")
            score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] + chlng
            #score[(2 * opp) - 1 + rpmd] = score[(2 * opp) - 1 + rpmd] - gnlhc
        elif pcroll < oproll:
            if args.verbose:
                print("LOSE!")
            #score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] - chlng
            score[(2 * opp) - 1 + rpmd] = score[(2 * opp) - 1 + rpmd] + gnlhc
        elif pcroll == oproll:
            if args.verbose:
                print("TIE!")
            if tiebreak() == True:
                if args.verbose:
                    print("WIN!")
                score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] + chlng
                #score[(2 * opp) - 1 + rpmd] = score[(2 * opp) - 1 + rpmd] - gnlhc
            else:
                if args.verbose:
                    print("LOSE!")
                #score[(2 * turn) - 1 + rpmd] = score[(2 * turn) - 1 + rpmd] - chlng
                score[(2 * opp) - 1 + rpmd] = score[(2 * opp) - 1 + rpmd] + gnlhc
        else:
            print("ERROR: pcroll or oproll is invalid!")


    # Results

    # If a score value is below zero at the end of a scene, bump up to zero.
    for checkms in score[1:]:
        if checkms < 0:
            score[score.index(checkms)] = MS

    # AI: Calculate each dice tier for all stats into an array (Overwrite array from last scene)
    tiers = []
    for scores in score[1:]:
        tiers.append(dicetier(scores))
    if args.verbose:
        print("Dice tiers for AI")
        print(tiers)

    # Score after each happening
    if args.verbose:
        print(','.join(map(str, score)))

    # Score after each event
    if turn == N:
        if args.verbose:
            print("Final event scores:")
        print(','.join(map(str, score)))
        writer.writerow(score)




# Events 1-6 are complete.
# Find winner or play event 7

# Calculate max Repuation and Madness after 6 events

# Make new arrays for Reputation and Madness
ev6rep = score[1::2]
ev6mad = score[2::2]

if args.verbose:
    print("Event 6 Reputation: " + str(ev6rep))
    print("Event 6 Madness: " + str(ev6mad))

mev6rep = max(ev6rep)
mev6mad = max(ev6mad)

print("Highest Reputation:," + str(mev6rep))
print("Highest Madness:," + str(mev6mad))

# Find player or players that have max scores
toprep = []
topmad = []

# Record player or players with highest reputation.
for i, j in enumerate(ev6rep):
    if j == mev6rep:
        toprep.append(i + 1)

# Record player or players with highest madness.
for i, j in enumerate(ev6mad):
    if j == mev6mad:
        topmad.append(i + 1)

print("Player(s) with highest Reputation:," + str(toprep))
print("Player(s) with highest Madness:," + str(topmad))

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
            print("WIN!")
        win = topmad[0]
    elif ev7mad < ev7rep:
        if args.verbose:
            print("LOSE!")
        win = toprep[0]
    elif ev7mad == ev7rep:
        if args.verbose:
            print("TIE!")
        if tiebreak() == True:
            if args.verbose:
                print("WIN!")
            win = topmad[0]
        else:
            if args.verbose:
                print("LOSE!")
            win = toprep[0]
else:
    win = "EVENT 7 EDGE CASE!"

# Report if there is a winner
print("Winner:," + str(win))




# Close csv file lock
file.close()

# (Optional) run python script on csv to graph results.
plotdicemechanic.plotaspng(filename)  # Python 3
