#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
l.sort()
for i in range(2,n):
    x=l[i-2]+l[i-1]
    if x>l[i]:
        print("YES")
        quit()
print("NO")
