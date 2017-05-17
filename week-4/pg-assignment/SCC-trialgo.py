#test1.txt Answer: 3,3,3,0,0
#test2.txt Answer: 3,3,2,0,0
#test3.txt Answer: 3,3,1,1,0
#test4.txt Answer: 7,1,0,0,0
#test5.txt Answer: 6,3,2,1,0 
"""
Class reprenstation of a oriented graph with non valuated vertex.
"""
class Graph():
    def __init__(self):
        self.adjList = {}
        self.numVertices = 0
        self.time={}
        self.leaders={}
        self.visited=[]
    def __iter__(self):
        return iter(self.adjList)
    def __getitem__(self,index):
        return self.adjList[index]
    def __setitem__(self,index,value):
        self.adjList[index] = value
    def __contains__(self,n):
        return n in self.adjList
    def __len__(self):
        return len(self.adjList)
    #def __reversed__(self):
    #    return 
    def __next__(self):
        next_value = self.value
        self.value += 2
        return next_value
    def addVertex(self,key):
        key=int(key)
        self.numVertices += 1
        self.adjList[key] = list()

    def getVertex(self,n):
        if n in self.vertList:
            return self.adjList[n]
        else:
            return None

    def getLength(self):
        return self.numVertices

    def addEdge(self,f,t):
        f=int(f)
        t=int(t)
        if f not in self.getVertices():
            self.addVertex(f)
        if t not in self.getVertices():
            self.addVertex(t)
        self.adjList[f].append(t)
    def getVertices(self):
        return list(self.adjList.keys())
def dfs_iterative(G, to_visit):
    """DFS, detect connected component, iterative implementation
    :param graph: directed graph in listlist or listdict format
    :param int node: to start graph exploration
    :param boolean-table seen: will be set true for the connected component
          containing node.
    :complexity: `O(|V|+|E|)`
    """
    t=1
    while to_visit:
        node = to_visit.pop()
        G.visited.append(node)
        print('node: '+str(node)+' time: '+str(t))
        G.time[node]=t
        t+=1
        for neighbor in G[node]:
            if neighbor not in G.visited:
                G.visited.append(node)
                to_visit.append(neighbor)
def SCC(G,revG):
    """
    First DFL-LOOP:
    run DFS on reverse graph and copute finishiing time for each node
    """
    to_visit=[G.getVertices()[0]]
    print(str(to_visit))
    dfs_iterative(revG,to_visit)
    print(str(G.time))
    """
    Second DFL-LOOP:
    run DFS on initial graph in decreasing order of 1st loop finishing
    time,and compute leader for each node
    """
from collections import OrderedDict,deque
import time
start=time.time()
G=Graph()
revG=Graph()
edges=[[1,4],[2,8],[3,6],[4,7],[5,2],[6,9],[7,1],[8,5],[8,6],[9,7],[9,3]]
edges_test_2=[[1,2],[2,3],[2,4],[2,5],[3,6],[4,5],[4,7],[5,2],[5,6],[5,7],[6,3],[6,8],[7,8],[7,10],[8,7],[9,7],[10,9],[10,11],[11,12],[12,10]]
for edge in edges:
    G.addEdge(edge[0],edge[1]) 
    revG.addEdge(edge[1],edge[0])    
#answer=OrderedDict(sorted(SCC(G,revG).items(), key=lambda t: t[1],reverse=True))
SCC(G,revG)
#print('answer: '+str(answer))
end=(start+time.time())
print(str(end))