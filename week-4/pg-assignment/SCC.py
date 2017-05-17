from collections import defaultdict,deque,OrderedDict
import sys
import time
import resource

class Vertex:
    def __init__(self,key):
        self.id = int(key)
        self.connectedTo = []
        self.visited=-1

    def addNeighbor(self,nbr):
        self.connectedTo.append(nbr)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo
    def getId(self):
        return self.id
    def getVisited(self):
        return self.visited
    def setVisited(self,val):
        self.visited=val

class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        key=int(key)
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t):
        f=int(f)
        t=int(t)
        if f not in self.getVertices():
            nv = self.addVertex(f)
        if t not in self.getVertices():
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.revind=dict()
        self.scc=dict()
        self.currentLeader=0
        self.dfs()
    def dfs(self):
        #self.order
        #import pdb; pdb.set_trace()
        #print('i''m in dfs')
        for aVertex in self:
            if aVertex.getVisited() == -1:
                self.dfsVisit(aVertex)
    def dfsOrdered(self):
        #print('i''m in dfs ordered')
        keys=list(self.revind.keys())
        #print('revind: '+str(self.revind))
        while len(keys)>0:
            k=keys.pop()
            aVertex=self.getVertex(self.revind[k])
            if aVertex.getVisited() == -1:                
                self.dfsVisitOrdered(aVertex)
                self.currentLeader=aVertex.getId()
                self.scc[self.currentLeader]=self.time
                self.time=0
                #print('key: '+str(k)+' vertex id: '+str(self.currentLeader)+': '+str(self.scc[self.currentLeader]))           
    def dfsVisit(self,startVertex):
        startVertex.setVisited(1)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getVisited() == -1:
                self.dfsVisit(nextVertex)
        startVertex.setVisited(1)
        self.time += 1
        #print(str(startVertex.getId())+': '+str(self.time))
        self.revind[self.time]=startVertex.getId()
    def dfsVisitOrdered(self,startVertex):
        startVertex.setVisited(1)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getVisited() == -1:
                self.dfsVisitOrdered(nextVertex)
        startVertex.setVisited(1)
        self.time += 1
    def reverseGraph(self):
        revG=DFSGraph()
        for aVertex in self:
            aVertex.setVisited(-1)
            for conn in aVertex.getConnections():
                revG.addEdge(conn.getId(),aVertex.getId())
        #revG.time=self.time
        return revG


start=time.time()
#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 24, 2 ** 24))
path='SCC.txt'
with open(path) as file:
    G=DFSGraph()
    revG=DFSGraph()
    edges=[]
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        edge=line.rstrip().split(' ')
        G.addEdge(edge[0],edge[1])
        revG.addEdge(edge[1],edge[0])
    revG.dfs()
    G.revind=revG.revind
    G.dfsOrdered()
    answer=OrderedDict(sorted(G.scc.items(), key=lambda t: t[1],reverse=True)[:5])
    print('answer: '+str(answer))
end=(start+time.time())
print(str(end))
