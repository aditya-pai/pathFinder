###PLEASE RUN USING PYTHON3
###AUTHOR: ADITYA D PAI

import heapq as hp
import sim2
import sys
import random
from termcolor import colored

#Implementation of Priority Queue using Heap data structure
class PQ:                                           
    def __init__(self):                             #Constructor
        self.items = []

    def insert(self, node, priority):               #Add to Priority Queue
        hp.heappush(self.items, (priority, node))
    
    def get(self):                                  #Retrieve from Priority Queue
        return hp.heappop(self.items)[1]
    
    def isEmpty(self):                              #Check if Queue is empty
        if len(self.items) == 0:
            return 1
        else:
            return 0

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

#Retrieve cost of cell; defaults to 1 if not explicitly weighted
def getCost(a,weightedCells):
    return weightedCells.get(a, 1)

#Function to find least cost path 
def findPath2(): 
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
    obstacles,start,goal,weightedCells=sim2.getGrid(size) 
    prev = {}
    isFound=False
    prev[start] = None
    cost = {}
    cost[start] = 0  
    lead = PQ()
    lead.insert(start, 0)
    while not lead.isEmpty():
        cell = lead.get()       
        if cell == goal:
            isFound=True
            break       
        for next in checkAdj(size,cell,obstacles):              #Check for candidate cells from neighbors
            g_x = cost[cell] + getCost(next,weightedCells)      #Get current cost
            if next not in cost or g_x < cost[next]:            #considering only new, low cost cells
                cost[next] = g_x
                (x1, y1) = goal                                 
                (x2, y2) = next                                 
                h_x=abs(x1 - x2) + abs(y1 - y2)                 #Calculate Admissable Heurstic Function    
                f_x = g_x  + h_x                                #total cost= current cost + cost to goal 
                lead.insert(next, f_x)
                prev[next] = cell                               #update path list
    return prev, cost, start, goal, size, obstacles, weightedCells, isFound

prev, cost, start, goal, size, obstacles, weightedCells,isFound = findPath2()
#function for Printing the formatted Grid based on inputs
def printGrid(size,obstacles,start,goal,weightedCells, **var):
    print("Start: ",start,"\n")
    print("Goal: ",goal,"\n")

    (w,h)=size
    for x in range(w):
        for y in range(h):
            index=(x,y)
            el = ". "
            if index in weightedCells:
                el=str(getCost(index,weightedCells))+' '        #Print weights on grid
            if index in obstacles:                      #Prints obstacles
                el = "X "
            if 'route' in var:                          #Print route
                if index in var['route']: 
                    el = "o "
            if index==goal:                             #Print Goal cell
                el='G '
            if index==start:                            #Print Start cell
                el='S '
            if el == "o ":
                print(colored(el,'green'), end="")
            elif el == ". ":
                print(colored(el,'white'), end="")
            elif el == "X ":
                print(colored(el,'red'), end="")
            elif el == "S " or el=="G ":
                print(colored(el,'cyan'), end="")
            else:
                print(colored(el,'blue'), end="")
        print("  ",x)                                   #Print row number

#Retrieve traversed path from path list
def getPath(prev, start, goal):
    cell = goal
    route = [cell]
    while cell != start:                    #Loop till start reached from goal
        cell = prev[cell]
        route.append(cell)
    return route

#Display for feasible path to goal
if not isFound:
    printGrid(size,obstacles,start,goal,weightedCells)
    print("No path available")   
else:
    printGrid(size,obstacles,start,goal,weightedCells)
    print()
    #Print grid with path found
    printGrid(size,obstacles,start,goal,weightedCells, route=getPath(prev, start, goal))

