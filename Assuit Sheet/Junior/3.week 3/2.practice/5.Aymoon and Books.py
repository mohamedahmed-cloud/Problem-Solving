import sys,math,bisect,itertools
from collections import deque
import heapq
n=int(sys.stdin.readline())
arr=deque(map(int,sys.stdin.readline().split()))
t=int(sys.stdin.readline())
table=[]
for i in range(t):
    s=sys.stdin.readline().strip()
    # print(table)

    if s=="L" and arr:
        a=arr.popleft()
        heapq.heappush(table,-a)
    elif s=="R" and arr:
        a=arr.pop()
        heapq.heappush(table,-a)
    elif s=="Q":
        if table:
            print(-heapq.heappop(table))
        else:
            print(-1)
    