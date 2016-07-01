----------REAMDE---------------

------Author: ADITYA D PAI-----


This folder contains the following files:
1. gridSolver.py
2. sim1.py
3. bfs.py
4. sim2.py
5. aStar.py
6. unitTest.py



gridSolver.py provides an interface that invokes the algorithm based on user input.

sim1.py is the simulator required by the first part of the problem.

bfs.py is the script with the algorithm that solves the grid produced by the method defined in sim.py.

sim2.py is the simulator with extended dynamics(weights added).

aStar.py is the script with the algorithm that solves the grid produced by the method defined in sim2.py.

unitTest.py contains unit tests for certain methods of algo2.py and sim2.py.





RUNNING INSTRUCTIONS:

Please run all files using PYTHON 3
The scripts meant to be run are:

gridSolver.py
bfs.py
aStar.py

The scripts can be run with command line parameters, for defining the dimensions of the grid.

Eg: python <filename> <arg1> <arg2>

Note: Invalid arguments will result in defaulting to random values.



KEY to GRID:

'-' : Free Cell (Weight=1 in sim2.py)

X : Obstacle

(cell with number) : Weight of the particular cell 

S : Start Cell

G : Goal Cell

o : Path defining element
