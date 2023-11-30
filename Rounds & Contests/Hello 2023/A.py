#    Author : Mohamed Yousef 
#    Date   : 2023-06-26
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    n = test()
    s = svalues()
    flag = True
    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            print(0)
            flag = False
            break
        if s[i] == "L" and s[i + 1] == "R":
            print(i + 1)
            flag = False
            break
    if flag:
        print(-1)

