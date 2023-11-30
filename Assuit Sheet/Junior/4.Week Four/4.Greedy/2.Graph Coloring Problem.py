#    Author : Mohamed Yousef 
#    Date   : 2022-12-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
# Can't Understand problem yet...

# n=int(input())
jobs=list(map(int,sys.stdin.readline().split()))
profits=list(map(int,sys.stdin.readline().split()))
n=len(jobs)
all=[0]*n
for i in range(n):
    all[i]=[profits[i],jobs[i]]
all.sort(reverse=True)
print(all)
check=[0]*max(jobs)
ans=0
for i in range(n):
    if check[all[i][1]-1]==0:
        check[all[i][1]-1]=1
        ans+=all[i][0]
        print(all[i][0])
        # print(check)
    else:
        j=1
        while j<=all[i][1] and all[i][1]-j-1>=0:
            if check[all[i][1]-j-1]==0:
                check[all[i][1]-j-1]=1
                ans+=all[i][0]
                break
            # print(check,"from here")
            j+=1

print(check)
print(ans)