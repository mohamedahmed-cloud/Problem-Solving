#    Author : Mohamed Yousef 
#    Date   : 2023-12-14
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

# Another Excellent Solution
sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

x,y,m = mvalues()

diff = float("inf")
for i in range(m // y + 1):
    diff = min(diff, (m - i * y) % x)
print(m - diff)
