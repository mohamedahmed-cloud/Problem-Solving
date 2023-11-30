#    Author : Mohamed Yousef 
#    Date   : 2022-12-19
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    l=list(map(int,sys.stdin.readline().split()))
    a=l[0]
    b=l[0]
    for i in range(1,n):
        a=a | l[i]
        b=b & l[i]
    print(a-b)

    