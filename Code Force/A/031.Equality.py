#    Author : Mohamed Yousef 
#    Date   : 2023-02-01
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
m,n=map(int,sys.stdin.readline().split())
s=sys.stdin.readline().strip()
arr=[0]*n
for i in s:
    arr[ord(i)-ord("A")]+=1
print(n*min(arr))

