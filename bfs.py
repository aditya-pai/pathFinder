###PLEASE RUN USING PYTHON3
###AUTHOR: ADITYA D PAI

import heapq as hp
import sim1 as sim
import sys
import random
import collections
#import sim2 

class Queue:
    def __init__(self):                     #Constructor
        self.items = collections.deque()
    
    def insert(self, x):                    #Add to queue
        self.items.append(x)
    
    def get(self):                          #Retrieve from queue
        return self.items.popleft()
    
    def isEmpty(self):                      #Check if queue is empty
        return len(self.items) == 0


#Find adjacent cells that are clear
def checkAdj(size,index,obstacles):                 
    (x, y) = index
    (w,h)=size
    adj = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]  #List of adjacent cells
    temp=[]
    for el in adj:
        (p,q)=el
        if 0 <= p < w and 0 <= q < h:               #Check if within grid limits
            temp.append(el)
    clear=[]
    for el in temp:
        if el not in obstacles:                     #Check if within free space
            clear.append(el)
    return clear

#Function to find shortest path
def findPath(): 
    #Check for valid command-line arguments, otherwise set default
    if len(sys.argv)<3 or sys.argv[1]==None or not str.isnumeric(sys.argv[1]):
        height=random.randint(10,20)
    else:
        height=int(sys.argv[1])
    if len(sys.argv)<3 or sys.argv[2]==None or not str.isnumeric(sys.argv[2]):
        width=random.randint(10,20)
    else:
        width=int(sys.argv[2])
    size=(width,height)
#Retrieving Grid data from function that creates the grid
    obstacles,start,goal=sim.getGrid(size)
    (h,w)=size
    lead = Queue()
    lead.insert(start)
    isFound=False
    prev = {}
    prev[start] = None
    while not lead.isEmpty():
        cell = lead.get()       
        if cell == goal:
            isFound=True
            break       
        for next in checkAdj(size,cell,obstacles):      #check candidate cells from neighbors
            if next not in prev:                        #considering only new cells
                lead.insert(next)
                prev[next] = cell                       #Update path list
    return prev, start, goal, size, obstacles, isFound

prev, start, goal,size, obstacles, isFound = findPath()
#function for Printing the formatted Grid based on inputs
def printGrid(size,obstacles,start,goal, **var):
    print("Start: ",start,'\n')
    print("Goal: ",goal,'\n')

    (w,h)=size
    for x in range(w):
        for y in range(h):
            index=(x,y)
            el = "- "
            if index in obstacles:                  #Prints obstacles
                el = "X "
            if 'route' in var:                      #prints route taken
                if index in var['route']: 
                    el = "o "
            if index==goal:                         #Prints goal cell
                el='G '
            if index==start:                        #Prints start cell
                el='S '
            print(el, end="")
        print("  ",x)                               #Print row number

#Retrieve traversed path from path list
def getPath(prev, start, goal):
    cell = goal
    route = [cell]
    while cell != start:                #Loop till start reached from goal
        cell = prev[cell]
        route.append(cell)
    return route

#Display for feasible path to goal
if not isFound:     
    printGrid(size,obstacles,start,goal)
    print("No path available")   
else:
    printGrid(size,obstacles,start,goal)
    print()
    #Print grid with path found
    printGrid(size,obstacles,start,goal, route=getPath(prev, start, goal))

