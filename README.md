# Signalis - Pump Puzzle solver

The game Signalis features a puzzle dubbed the "Pump Puzzle". This repository contains a simple leetcode-style program that searches for solutions using a breadth-first graph traversal method.

To run it, just do:

```bash
python main.py
```

Found solutions up to 9 steps:

```
Solution 0: 7 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 1: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=0, b=8, c=4)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 2: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 3: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 4: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 5: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 6: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 7: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 8: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=7, b=0, c=5)
  PumpState(a=12, b=0, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
Solution 9: 9 steps
  PumpState(a=12, b=0, c=0)
  PumpState(a=7, b=0, c=5)
  PumpState(a=7, b=5, c=0)
  PumpState(a=4, b=8, c=0)
  PumpState(a=4, b=3, c=5)
  PumpState(a=9, b=3, c=0)
  PumpState(a=9, b=0, c=3)
  PumpState(a=1, b=8, c=3)
  PumpState(a=1, b=6, c=5)
  PumpState(a=6, b=6, c=0)
```
