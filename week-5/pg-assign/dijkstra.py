import math as m
import heapq as hp
from unittest import TestCase
"""
Heap structure
parent(i)       
    if i even= i/2
    elif i odd= [i/2] (i.e round down)
children(i)=2i and 2i+1
"""
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
"""
def dijkstra(root,adjList,shortest):
    
    shortest[root]=0
    visited=set()
    next=[]# heap list of "shortest paths", can have multiple path for one node
    hp.heappush(next,(0,root))
    while len(visited)!=len(adjList):
        current=hp.heappop(next)
        if current[1] in visited:
            continue
        """
        visited.add(current) guarantee to add a shortest path (pop of the current heap)
        """
        visited.add(current)
        #print(str(next))
        #print(current[1])
        #print(str(adjList[current[1]]))
        for neighbour,distN in adjList[current[1]]:
            if neighbour in visited:
                continue
            newShort=shortest[current[1]]+distN
            if (neighbour not in shortest) or (newShort<shortest[neighbour]):
                shortest[neighbour]=newShort
                hp.heappush(next,(newShort,neighbour))
    return shortest
                
def main(path):
    """
    adjList: dictionnary of valuated vertex
    (key: int repr of vertex v, 
    val: []a list of valuated node connected to v )
    """
    adjList=dict()
    #useful for parsing file
    vertex=[]
    """
    shortest : shortest paths for every element of X
    """
    shortest=dict()
    
    with open(path) as f:
        for line in f:
            vertex=[e for e in line.rstrip().split('\t')]
            #print(str(vertex[1:]))
            adjList[int(vertex[0])]=[]
            shortest[int(vertex[0])]=m.inf
            for e in vertex[1:]:
                val=[i for i in e.split(',')]
                val=(int(val[0]),int(val[1]))
                adjList[int(vertex[0])].append(val)
            #print("node: "+vertex[0]+" adjList: "+str(adjList[vertex[0]]))
        shortest=dijkstra(1,adjList,shortest)
        return shortest

path='dijkstraData.txt'
shortest=main(path)
request=[7,37,59,82,99,115,133,165,188,197]
answer=""
for e in request:
    answer=answer+(str(shortest[e])+',')
print(answer)    
    #print(str(adjList[vertex[0]]))
"""
class TestDijkstra(TestCase):
    def check(self, path,expected):
        found=main(path)
        
        self.assertEqual(expected, found)
    def runTest(self):
        expected={1:0,2:1,3:2,4:3,5:4,6:4,7:3,8:2}
        self.check('test1.txt',expected)
"""