#    Author : Mohamed Yousef 
#    Date   : 2022-12-29
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py

# https://leetcode.com/problems/maximum-width-of-binary-tree/
def solve(root):
    n=len(root)
    depth=0
    j=1
    for i in range(n,j):
        if i==j:
            depth+=1
        for x in range(j):
            if root[i]==None:
                j-=1
        j*=2
    print(j)
    return depth
print(solve( [1,3,2,5,None,None,9,6,None,7]))