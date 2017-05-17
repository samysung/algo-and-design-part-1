def partition(mylist, start, end, count):
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i],mylist[pos] = mylist[pos],mylist[i]
            pos += 1
    mylist[pos],mylist[end] = mylist[end],mylist[pos]
    return pos, count

def quicksort(mylist, start, end, count):
    if start < end:
        pos, count = partition(mylist, start, end, count)        
        count = quicksort(mylist, start, pos - 1, count)
        count = quicksort(mylist, pos + 1, end, count)
    return count


path='quicksort.txt'
with open(path) as file:
    lines = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        lines.append(line.rstrip())
    A = list(map(int, lines))
B=[3,9,8,4,6,10,2,5,7,1]
count = quicksort(A, 0, len(A)-1, 0)
print (A,count)

