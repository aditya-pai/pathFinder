###PLEASE RUN USING PYTHON3
###AUTHOR: ADITYA D PAI

import unittest
from algo2 import findPath2
from sim2 import getGrid
class pathTest(unittest.TestCase):
	def test_pathFound(self):
		prev, cost, start, goal,size, obstacles,  weightedCells,isFound  = findPath2()
		self.assertTrue(isFound)
		print("\nSuccess")

	def test_goalWithinGrid(self):
		size=(100,100)
		obstacles,start,goal,weightedCells=getGrid(size)
		self.assertLess(goal,size)
		print("\nSuccess")
	
	def test_startWithinGrid(self):
		size=(100,100)
		obstacles,start,goal,weightedCells=getGrid(size)
		self.assertLess(start,size)
		print("\nSuccess")

	def test_startNotInObstacles(self):
		size=(100,100)
		obstacles,start,goal,weightedCells=getGrid(size)
		self.assertNotIn(start,obstacles)
		print("\nSuccess")

	def test_goalNotInObstacles(self):
		size=(100,100)
		obstacles,start,goal,weightedCells=getGrid(size)
		self.assertNotIn(goal,obstacles)
		print("\nSuccess")

	def test_startNotEqualGoal(self):
		size=(100,100)
		obstacles,start,goal,weightedCells=getGrid(size)
		self.assertNotEqual(start,goal)
		print("\nSuccess")

if __name__ == '__main__': 
	unittest.main()