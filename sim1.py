###PLEASE RUN USING PYTHON3
###AUTHOR: ADITYA D PAI

import random

def getGrid(size):
	(width,height)=size
	obstacles=[]
	count=int(height*(random.randint(height-1,height+5)/10))
	for i in range (0,count):
		Ox=random.randint(0,width-1)
		Oy=random.randint(0,height-1)
		index=(Ox,Oy)
		obstacles.append(index)

	Sx=random.randint(0,width-1)
	Sy=random.randint(0,height-1)
	Gx=random.randint(0,width-1)
	Gy=random.randint(0,height-1)
	start=(Sx,Sy)
	goal=(Gx,Gy)

	while start in obstacles:
		Sx=random.randint(0,width-1)
		Sy=random.randint(0,height-1)	
		start=(Sx,Sy)

	while start==goal or goal in obstacles:
		Gx=random.randint(0,width-1)
		Gy=random.randint(0,height-1)
		goal=(Gx,Gy)
	return obstacles,start,goal
