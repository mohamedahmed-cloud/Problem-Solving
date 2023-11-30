#    Author : Mohamed Yousef 
#    Date   : 2022-12-05
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
k=int(sys.stdin.readline())
ans=10
while k:
    ans+=9
    if sum(map(int,str(ans)))==10:
        k-=1
print(ans)



