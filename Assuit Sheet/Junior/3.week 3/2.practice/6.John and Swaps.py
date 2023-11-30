import sys,math,bisect,itertools
from collections import deque
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    l=list(map(int,sys.stdin.readline().split()))
    s=l.copy()
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            l[i],l[j]=l[j],l[i]
            ans.add(tuple(l))
            l[i],l[j]=l[j],l[i]
    print(len(ans))
