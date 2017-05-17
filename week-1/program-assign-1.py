# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

# Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.

# Because of the large size of this array, you should implement the fast divide-and-conquer algorithm 
#covered in the video lectures.

# The numeric answer for the given input file should be typed in the space below.
# So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks.
# You can make up to 5 attempts, and we'll use the best one for grading.
# (We do not require you to submit your code, so feel free to use any programming language you want ---
# just type the final numeric answer in the following space.)

# [TIP: before submitting, first test the correctness of your program on some small test files or your own devising. 
#Then post your best test cases to the discussion forums to help your fellow students!]
from itertools import combinations
from random import randrange
from unittest import TestCase

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def merge_and_count_inversions(seq, start, middle, end):
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
    inversions = 0
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
            inversions += middle - i
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
	 
def sort_and_count_inversions(seq):
    #Sort a sequence and count inversions.

    #Argument: seq -- a sequence

    #Result: number of inversions (cases where i < j, but seq[i] > seq[j]).

    #Side effect: seq is sorted.

    
    def sort_and_count(seq, start, end):
        if end - start < 2:
            return 0
        middle = (start + end) // 2
        return (sort_and_count(seq, start, middle)
                + sort_and_count(seq, middle, end)
                + merge_and_count_inversions(seq, start, middle, end))
    result=sort_and_count(seq, 0, len(seq))
    print(result)
    return result


class TestSortAndCount(TestCase):
    def check(self, seq):
        expected = sum(j < i for i, j in combinations(seq, 2))
        found = sort_and_count_inversions(seq)
        self.assertEqual(expected, found)
        self.assertEqual(seq, sorted(seq))

    def runTest(self):
        self.check([])                    # empty sequence
        self.check([1])                   # single element
        self.check([1, 3, 5, 2, 4, 6])    # even length
        self.check([1, 3, 5, 2, 4, 6, 3]) # odd length, duplicate value
        for _ in range(100):              # random test cases
            self.check([randrange(100) for _ in range(randrange(100))])


path='IntegerArray.txt'
#
n=file_len(path)#number of line/number
l=[ 4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ]
sort_and_count_inversions(l)
#q=0
with open(path) as file:
    lines = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        lines.append(line.rstrip())
    numbers = list(map(int, lines))
    sort_and_count_inversions(numbers)
    print(len(lines))
    file.close()
