from collections import defaultdict,deque,OrderedDict
#from Set import set
import time

class Vertex:
    def __init__(self,key):
        self.id = int(key)
        self.connectedTo = set()
        self.visited=-1

    def addNeighbor(self,nbr):
        self.connectedTo.add(nbr)

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
        self.nodes=set()

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
        for aVertex in self:
            if aVertex.getVisited() == -1:
                print('i''m in dfs')
                self.dfsVisit(aVertex)
    def dfsOrdered(self):
        print('i''m in dfs ordered')
        keys=list(self.revind.keys())
        print('revind: '+str(self.revind))
        while len(keys)>0:
            k=keys.pop()
            aVertex=self.getVertex(self.revind[k])
            if aVertex.getVisited() == -1:                
                self.dfsVisitOrdered(aVertex)
                self.currentLeader=aVertex.getId()
                self.scc[self.currentLeader]=self.time
                self.time=0
                print('key: '+str(k)+' vertex id: '+str(self.currentLeader)+': '+str(self.scc[self.currentLeader]))           
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
G=DFSGraph()
revG=DFSGraph()
edges=[[1,4],[2,8],[3,6],[4,7],[5,2],[6,9],[7,1],[8,5],[8,6],[9,7],[9,3]]
edges_test_2=[[1,2],[2,3],[2,4],[2,5],[3,6],[4,5],[4,7],[5,2],[5,6],[5,7],[6,3],[6,8],[7,8],[7,10],[8,7],[9,7],[10,9],[10,11],[11,12],[12,10]]
for edge in edges_test_2:
  G.addEdge(edge[0],edge[1])
  revG.addEdge(edge[1],edge[0])
#revG=G.reverseGraph()
revG.dfs()
G.revind=revG.revind
G.dfsOrdered()
for v in G:
    print('vertex number: '+str(v.getId()))
print(str(G.scc))
for ind,val in G.scc.items():
    print('SCC with leader '+str(ind)+': '+str(G.scc[ind]))
end=(start+time.time())
answer=OrderedDict(sorted(G.scc.items(), key=lambda t: t[1],reverse=True)[:5])
print('answer: '+str(answer))
print(str(end))