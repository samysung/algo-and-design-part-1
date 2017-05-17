numL=[]
results=set()#use a container that gets rid of duplicates
with open('2sum.txt') as f:
    for line in f:
        numL.append(int(line.rstrip()))    
    nums=sorted(list(map(int, numL)))
    leftindex=0
    rightindex=len(nums)-1
    rightlast=False
    while rightindex>leftindex:
      sum=nums[rightindex]+nums[leftindex]
      if sum<(-10000):
        leftindex+=1
        rightlast=False
      elif sum>10000:
        rightindex-=1
        rightlast=True
      else: 
          if rightlast==True:
              tempindex=leftindex
              while sum<10001:
                  results.add(sum)
                  tempindex+=1
                  sum=nums[tempindex]+nums[rightindex]
              rightindex-=1
          else:
              tempindex=rightindex
              while(sum>-10001):
                  results.add(sum)
                  tempindex-=1
                  sum=nums[tempindex]+nums[leftindex]
              leftindex+=1
print(str(len(results)))

#answer 427