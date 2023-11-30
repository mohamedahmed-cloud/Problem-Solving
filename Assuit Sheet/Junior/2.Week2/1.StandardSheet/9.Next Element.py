# time limit.
import sys,math,bisect,itertools
from collections import deque
n=int(sys.stdin.readline())
arr=deque(map(int,sys.stdin.readline().split()))
stack=deque()
ans=[-1]*n
for i in range(n):
    while stack and arr[i]>arr[stack[-1]]:
        ans[stack[-1]]=i+1
        stack.pop()
    stack.append(i)
q=int(input())
for i in range(q):
    x=int(input())
    out=ans[x-1]
    sys.stdout.write(str(out)+"\n")