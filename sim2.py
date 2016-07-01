###PLEASE RUN USING PYTHON3
###AUTHOR: ADITYA D PAI
###------GRID SPACE SIMULATOR-------
import random
import sys
def getGrid(size):
	(width,height)=size
	obstacles=[]
	count=int(height*(random.randint(height-1,height+5)/10))
	for i in range (0,count):
		origin_x=random.randint(0,width-1)
		origin_y=random.randint(0,height-1)
		index=(origin_x,origin_y)
		obstacles.append(index)
	
	weight_list = {}
	weight_count=int(height*(random.randint(height-1,height+5)/5))
	for i in range (0,weight_count):
		weight_x=random.randint(0,width-1)
		weight_y=random.randint(0,height-1)
		weight=(weight_x,weight_y)
		weight_list.update({weight:random.randint(3,7)})

	start_x=random.randint(0,width-1)
	start_y=random.randint(0,height-1)
	goal_x=random.randint(0,width-1)
	goal_y=random.randint(0,height-1)
	start=(start_x,start_y)
	goal=(goal_x,goal_y)

	while start in obstacles:
		start_x=random.randint(0,width-1)
		start_y=random.randint(0,height-1)	
		start=(start_x,start_y)

	while start==goal or goal in obstacles:
		goal_x=random.randint(0,width-1)
		goal_y=random.randint(0,height-1)
		goal=(goal_x,goal_y)

	return obstacles,start,goal,weight_list

