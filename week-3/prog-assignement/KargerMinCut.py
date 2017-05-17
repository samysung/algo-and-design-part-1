import random
def pickEdge(sparseL):
    V1=random.choice(sparseL)
    indV1=V1[0]
    rE=int(random.choice(V1[1:len(l)-1]))
    print('liste: '+str(l))
    print ('len rV: '+str(rV))
    print ('rE: '+str(rE))
    return rV,rE

def mergeVertices(V1,V2,sparseL):
    l=[v for v in sparseL[V2-1] if (v!=V1) & (v!=V2)]
    for ind,v in enumerate(l):
        updateNeighbour(v-1,sparseL,V1,V2)
        sparseL[V1].append(v) 
    return deleteSelfLoop(V1,V2,sparseL)
def updateNeighbour(v,sparseL,new,old):
	l=sparseL[int(v)]
	for idx, edges in enumerate(l):
		if old==edges:
			#item = replace_all(...)
			l[idx] = new
def deleteSelfLoop(V1,V2,sparseL):
	if V2 in sparseL[V1]: sparseL[V1].remove(V2)
	return sparseL
def cut(sparseL):
	if len(sparseL)>2:
		V1,V2=pickEdge(sparseL)
		sparseL=mergeVertices(V1,V2,sparseL)
		return cut(sparseL)
	return len(sparseL[0])

def minCut(sparseL):
	mincut=cut(sparseL)
	return minCut


def merge(seq, start, middle, end):
	# """Merge two adjacent sorted sub-sequences of seq and count
    #    inversions.

    #    Arguments: 
    #    seq -- sequence to sort
    #    start -- index of beginning of first sorted subsequence
    #    middle -- end of first, and beginning of second, sorted subsequence
    #    end -- end of second sorted subsequence

    #    Result: number of inversions (cases where i < j, but seq[i] > seq[j]).

    #    Side effect: seq is sorted between start and end.

    #    """
    assert 0 <= start < middle < end <= len(seq)
    #inversions = 0
    temp = []
    i = start
    j = middle
    while i < middle and j < end:
        if  seq[i] <= seq[j]:
            temp.append(seq[i])
            i += 1
        else:
            temp.append(seq[j])
            j += 1
            #inversions += middle - i
    if j == end:
        # Second subsequence is complete: process remainder of first.
        temp.extend(seq[i:middle])
    else:
        # First subsequence is complete: no need to process
        # remaininder of second, since it does not move.
        pass
    # Insert sorted results into original sequence.
    seq[start:start+len(temp)] = temp
    return inversions
	 
def sort_helper(seq):
    #Sort a sequence and count inversions.

    #Argument: seq -- a sequence

    #Result: number of inversions (cases where i < j, but seq[i] > seq[j]).

    #Side effect: seq is sorted.   
    def sort(seq, start, end):
        if end - start < 2:
            return 0
        middle = (start + end) // 2
        return (sort(seq, start, middle)
                + sort(seq, middle, end)
                + merge(seq, start, middle, end))
    result=sort(seq, 0, len(seq))
    print(result)
    return seq



path='KargerMinCut.txt'
with open(path) as file:
    sparseL = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        sparseL.append(line.rstrip().split('\t'))
    for ind,e in enumerate(sparseL):
        #print('ligne '+str(ind)+': \n')
        for i,item in enumerate(sparseL[ind]):
            #print('vertices: '+item+';')
            sparseL[ind][i]=int(sparseL[ind][i])


    print(len(sparseL))
    minCut(sparseL)
    
#B=[3,9,8,4,6,10,2,5,7,1]
