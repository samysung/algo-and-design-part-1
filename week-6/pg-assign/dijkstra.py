import math
"""
Heap structure
parent(i)       
    if i even= i/2
    elif i odd= [i/2] (i.e round down)
children(i)=2i and 2i+1
"""
def swapWithParent(k):
	if k%2==0:
		numbers[k/2],numbers[k]=numbers[k],numbers[k/2]
	else:
		numbers[math.floor(k/2)],numbers[k]=numbers[k],numbers[math.floor(k/2)]

def bubleUp(k):
def bubbleDown(k):

def insert(k):
	numbers.append(k)

def lookUp:
def dijkstra():
	
medians=[]
sumMed=0
numbers=
with open('median.txt') as f:
    for line in f:
        numL.append(int(line.rstrip()))   