# Python-Puzzle-Solver
A star search for finding whether a given set of puzzle pieces fit within a NxM grid.

## Objective
This was a small personal project, with the purpose of implmenting an effective A star search in an effort to solve some puzzles. It was about consolidating tree searching methods and served as an introduction to the Tkinter Python library. I have since moved on from this project, as extensions and solutions would require massive amounts of refactoring and redesigning.

### Outstanding Problems
1. The GUI provided is very primitive and not user friendly
2. The task of calculating solutions does not run on a separate thread, which blocks I/O and causes the GUI to freeze
3. The GUI does not follow the Nielson's 10 heuristics for UI design, most notably:
> Visibility of system status

### Possible Extensions
1. Add counter for identical pieces, this would prune the number of expansions needed per leaf
2. Strict mode, which would disable the rotations of any piece
3. Machine learning approach over A star search, as with large grids the search struggles. However, training data would be required
