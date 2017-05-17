#QUESTION 3

#GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

#See the first question.

#DIRECTIONS FOR THIS PROBLEM:

#Compute the number of comparisons (as in Problem 1),
# using the "median-of-three" pivot rule. [The primary motivation behind this rule is to 
#do a little bit of extra work to get much better performance on input arrays that are nearly 
#sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first,
# middle, and final elements of the given array. (If the array has odd length it should be clear what 
#the "middle" element is; for an array with even length 2k, use the kth element as the "middle" element.
#So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of 
#these three elements is the median (i.e., the one whose value is in between the other two), and use this
# as your pivot. As discussed in the first and second parts of this programming assignment, be sure to 
#implement Partition exactly as described in the video lectures (including exchanging the pivot element 
#with the first element just before the main Partition subroutine).
#EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8),
#middle (4), and last (1) elements; since 4 is the median of the set {1,4,8},
# you would use 4 as your pivot element.

#ANSWER:138382
def quickSort(alist):
   global count
   count=0
   quickSortHelper(alist,0,len(alist)-1)
   print(count)
   
def quickSortHelper(alist,first,last):
   #global count
   if first<last:
      #count=count+last-2

       splitpoint = partition_1(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition_1(A,begin,end):
    global count
    count=count+len(A[begin:end])
    pivotInd=choose_pivot(A,begin,end)
    tmp=A[begin]
    A[begin]=A[pivotInd]
    A[pivotInd]=tmp
    p = A[begin]
    #if begin!=0:
      # A[begin]=A[0]
       #A[0]=p
    i=begin+1
    for j in range(begin+1, end+1):
        if A[j] < p:
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
            i += 1
    tmp=A[i-1]
    A[i-1] = A[begin]
    A[begin]=tmp
    return i-1
def choose_pivot(A,first,last):
  size=last-first+1
  if size<=2:
    return first
  if size%2==0:
    med=int(first+((size/2)-1))
  else:
    med=int(first+(size/2))
  if (A[first]<A[last]<A[med])or(A[med]<A[last]<A[first]):
    return last
  elif (A[first]<A[med]<A[last])or(A[last]<A[med]<A[first]):
    return med
  else:
    return first
def swap(A,i,j):
  tmp=0
  tmp=A[j]
  A[j]=A[i]
  A[i]=tmp
  return A
def partition(alist,first,last):
   pivotvalue = alist[first]
   global count
   count=count+len(A[first:last])-1
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
path='quicksort.txt'
with open(path) as file:
    lines = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        lines.append(line.rstrip())
    A = list(map(int, lines))
B=[3,9,8,4,6,10,2,5,7,1]
quickSort(A)
#print(B)