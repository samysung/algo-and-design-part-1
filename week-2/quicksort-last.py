#QUESTION 2
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
# See the first question.
# DIRECTIONS FOR THIS PROBLEM:
# Compute the number of comparisons (as in Problem 1),
# always using the final element of the given array as the pivot element. Again, be sure to implement
# the Partition subroutine exactly as it is described in the video lectures.
# Recall from the lectures that, just before the main Partition subroutine,
# you should exchange the pivot element (i.e., the last element) with the first element.
 #ANSWER: 164123

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
    tmp=A[begin]
    A[begin]=A[end]
    A[end]=tmp
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