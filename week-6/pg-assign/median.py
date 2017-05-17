import math
"""
parent(i)       
    if i even= i/2
    elif i odd= [i/2] (i.e round down)
children(i)=2i and 2i+1

CLRS page chapter 13.1 page 238-
"""
class node(object):
    def __init__(self,color,key,left,right,p):
	    self.color
	    self.key
	    self.left
	    self.right
	    self.p
class RBTree(object):
    def __init__(self):
	    self.tree=list()
    def __iter__(self):
    	return self.tree.values()
    def RBIinsert(T,z):
        return 0
    def RBIinsertFixup(T, z):
        return 0
    def RBDelete(T, z):
        return 0
    def RBDeleteFixup(T, z):
        return 0
    def LEFTRotate(T, x):
        return 0
    def RIGHTRotate(T, x):
        return 0
def median(numbers):
    numbers=sorted(numbers)
    l=len(numbers)-1
    if (l+1)%2==0:
        return numbers[int(l/2)]
    else:
        
        return numbers[int((l+1)/2)]

medians=[]
sumMed=0
numbers=[]
with open('median.txt') as f:
    for line in f:
        numbers.append(int(line.rstrip())) 
        medians.append(median(numbers))
print('sum of medians mod 1000: '+str((sum(medians))%10000))
#answer 1213