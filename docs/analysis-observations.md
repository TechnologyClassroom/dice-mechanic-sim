# Data Analysis Observations and Findings

- No point losses makes an interesting graph.

- Problem: No one gets to roll a d10 ever with this dice chart:

```
   1 -  6 = d6
   7 - 24 = d8
  25+     = d10
```

Proposed change: Lower d10 entry score.  New proposed chart:

```
   1 -  6 = d6
   7 - 13 = d8
  14+     = d10
```

- Problem: Negative scores come up regularly.  The rulebook does not address a
  minimum score or negative scores.

Solution: We need to add a minimum score to the rules.  The rule could read
something like, “If a player’s reputation or madness is below three at the
beginning of a new Happening or Event, bring that score back up to three.”
Three could be replaced with another number, but it is important that we have a
minimum score even if it is zero.

- Problem: Once reputation or madness reaches 0, there is little chance of
  recovering.

Solution: Experiment with higher minimum scores.

- Test runtime on UNIX based systems using this command:

```
time python3 dicemechanicsim.py
```
