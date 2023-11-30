#    Author : Mohamed Yousef 
#    Date   : 2023-01-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(s):
    myDict=defaultdict(int)
    n=len(s)-1
    i=0
    # while i<n:
        
