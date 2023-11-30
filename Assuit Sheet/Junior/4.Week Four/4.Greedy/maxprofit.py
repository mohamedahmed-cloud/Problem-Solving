#    Author : Mohamed Yousef 
#    Date   : 2022-12-31
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
jobs=list(map(int,sys.stdin.readline().split()))
profits=list(map(int,sys.stdin.readline().split()))
n=len(jobs)
store=[0]*n
for i in range(n):
    store[i]=[profits[i],jobs[i]]
store.sort(reverse=True)
mySet=set()
ans=0
for i in store:
    x=i[1]
    add=i[0]
    if x in mySet:
        while x>0:
            x-=1
            if x not in mySet and x>0:
                mySet.add(x)
                ans+=add
                break
    else:
        mySet.add(x)
        ans+=add
print(mySet)
print(ans)