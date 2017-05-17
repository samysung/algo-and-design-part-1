#QUESTION 1
# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) 
#in unsorted order. 
#The integer in the ith row of the file gives you the ith entry of an input array.
# Your task is to compute the total number of comparisons used to sort the given input 
#file by QuickSort. As you know, the number of comparisons depends on which elements
# are chosen as pivots, so we'll ask you to explore three different pivoting rules.
# You should not count comparisons one-by-one. Rather, when there is a recursive call
# on a subarray of length m, you should simply add m−1 to your running total of comparisons.
# (This is because the pivot element is compared to each of the other m−1 elements in the subarray 
#in this recursive call.)

# WARNING: The Partition subroutine can be implemented in several different ways, 
#and different implementations can give you differing numbers of comparisons. For this problem, 
#you should implement the Partition subroutine exactly as it is described in the video lectures
# (otherwise you might get the wrong answer).

# DIRECTIONS FOR THIS PROBLEM:

# For the first part of the programming assignment,
# you should always use the first element of the array as the pivot element.

# HOW TO GIVE US YOUR ANSWER:

# Type the numeric answer in the space provided.

# So if your answer is 1198233847, then just type 1198233847 in the space provided
# without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.

# (We do not require you to submit your code, so feel free to use the programming 
#language of your choice, just type the numeric answer in the following space.)

#ANSWER: 162085
count=0
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
    print(count)
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