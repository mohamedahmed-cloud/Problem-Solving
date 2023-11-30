#    Author : Mohamed Yousef 
#    Date   : 2023-02-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
from itertools  import accumulate ,combinations ,permutations 
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
t=test()
for i in range(t):
    n,k=mvalues()
    a=svalues()
    b=svalues()
    store=deque()
    cnt=0
    ans=0
    # idea -> First store all b in dict.
            # find each pair that have a max value
            # insert them in it right position
            # add value of two pair + "1" then increment answer by n(n+1)/2
    
