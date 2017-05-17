"""DFS.py

Algorithms for depth first search in Python.
We need to search iteratively rather than recursively in
order to avoid Python's low recursion limit.

D. Eppstein, July 2004.
"""

# Types of edges in DFS traversal.
# The numerical values are used in DepthFirstSearcher, change with care.
forward = 1     # traversing edge (v,w) from v to w
reverse = -1    # returning backwards on (v,w) from w to v
nontree = 0     # edge (v,w) is not part of the DFS tree
#leader=2
#nonleader=3
whole_graph = object()  # special flag object, do not use as a graph vertex

def search(G,iterG,initial_vertex = whole_graph,decreasing=True,t=0):
    """
    Generate sequence of triples (v,w,edgetype) for DFS of graph G.
    The subsequence for each root of each tree in the DFS forest starts
    with (root,root,forward) and ends with (root,root,reverse).
    If the initial vertex is given, it is used as the root and vertices
    not reachable from it are not searched.
    """
    visited = set()
    if initial_vertex == whole_graph:
        if decreasing:
            initials = reversed(list(iterG))
        else:
            initials = iterG
    else:
        initials = [initial_vertex]
    for v in initials:
        #print('v in for loop: '+str(v))
        if v not in visited:
            leader=v
            #print('leader:'+str(leader))
            visited.add(v)
            stack = [(v,iter(G[v]))]
            S=set(G[v])
            while stack:
                #stack[-1]: pick last in the list
                parent,children = stack[-1]
                #if parent not in visited:
                    #leader=parent
                #print('parent: '+str(parent))
                setChildren=set(G[v])
                try:
                    child = next(children)
                    if child not in visited:   
                        #leader=parent
                        visited.add(child)
                        stack.append((child,iter(G[child])))     
                except StopIteration:
                    #yield parent,leader,t 
                    t+=1
                    yield parent,leader,t
                    stack.pop()   
        #else:
            #yield v,leader,t
                    
                        
                        

                
        

def preOrder(G,initial_vertex = whole_graph):
    """Generate all vertices of graph G in depth-first preorder."""
    for v,l,t in search(G,initial_vertex):
        #print('ingoing: '+str(v)+' outgoing: '+str(w)+' leader: '+str(l))
        yield v,l,t

def postOrder(G,initial_vertex = whole_graph):
    """Generate all vertices of graph G in depth-first postorder."""
    for v,w,edgetype,l,t in search(G,initial_vertex):
        if edgetype is reverse:
            yield w,t

def SCC(G,revG):
    ordG=[]
    leaders={}
    print('FIRST LOOP.....')
    for v,l,t in search(revG,list(revG.getVertices())):
        #print(str(v))
        ordG.append(v)
        #print('time: '+str(t)+' v: '+str(v)+' adj of v: '+str(revG.adjList[v])+'leader: '+str(l))
    #print('ordG: '+str(ordG))
    print('SECOND LOOP.....')
    for v,l,t in search(G,ordG):
        #print('time: '+str(t)+' v: '+str(v)+' adj of v: '+str(G.adjList[v])+'leader: '+str(l))
        if l in leaders:
            leaders[l]+=1
        else:
            leaders[l]=1
    return leaders


class Searcher:
    """
    Handler for performing general depth first searches of graphs.
    Some or all of the routines preorder, postorder, and backedge
    should be shadowed in order to make the search do something useful.
    """

    def preorder(self,parent,child):
        """
        Called when DFS visits child, before visiting all grandchildren.
        Parent==child when child is the root of each DFS tree.
        """
        pass

    def postorder(self,parent,child):
        """
        Called when DFS visits child, after visiting all grandchildren.
        Parent==child when child is the root of each DFS tree.
        """
        pass

    def backedge(self,source,destination):
        """Called when DFS discovers an edge to a non-child."""
        pass

    def __init__(self,G):
        """Perform a depth first search of graph G."""
        dispatch = [self.backedge,self.preorder,self.postorder]
        for v,w,edgetype in search(G):
            dispatch[edgetype](v,w)
"""
Class reprenstation of a oriented graph with non valuated vertex.
"""
class Graph():
    def __init__(self):
        self.adjList = {}
        self.numVertices = 0
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
        return self.adjList.keys()

#test1.txt Answer: 3,3,3,0,0
#test2.txt Answer: 3,3,2,0,0
#test3.txt Answer: 3,3,1,1,0
#test4.txt Answer: 7,1,0,0,0
#test5.txt Answer: 6,3,2,1,0 
from collections import OrderedDict,deque
import time
 

G=Graph() 
revG=Graph() 
start=time.time()
path='SCC.txt'
print('FILE SCAN.....')
with open(path) as file:
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        edge=line.rstrip().split(' ')
        G.addEdge(edge[0],edge[1])
        revG.addEdge(edge[1],edge[0])
    print('END FILE SCAN.....')    
    answer=OrderedDict(sorted(SCC(G,revG).items(), key=lambda t: t[1],reverse=True))
    print('answer: '+str(answer))
end=(start+time.time())
print(str(end))


"""
434821,968,459,313,211
"""