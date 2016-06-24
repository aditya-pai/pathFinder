###PLEASE RUN USING PYTHON3
###AUTHOR: ADITYA D PAI

import random
import sys
def getGrid(size):
	(width,height)=size
	obstacles=[]
	count=int(height*(random.randint(height-1,height+5)/10))
	for i in range (0,count):
		Ox=random.randint(0,width-1)
		Oy=random.randint(0,height-1)
		index=(Ox,Oy)
		obstacles.append(index)
	
	weights = {}
	Wcount=int(height*(random.randint(height-1,height+5)/5))
	for i in range (0,Wcount):
		Wx=random.randint(0,width-1)
		Wy=random.randint(0,height-1)
		Windex=(Wx,Wy)
		weights.update({Windex:random.randint(3,7)})

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

	return obstacles,start,goal,weights

