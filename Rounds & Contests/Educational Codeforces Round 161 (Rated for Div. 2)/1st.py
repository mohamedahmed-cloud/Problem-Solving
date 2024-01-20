#    Author : Mohamed Yousef 
#    Date   : 2024-01-18
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
    s1 = svalues()
    s2 = svalues()
    s3 = svalues()
    flag = False

    for i in range(n):
        if s1[i] == s2[i] and s1[i] != s3[i] or (s1[i] != s2[i] and s1[i] != s3[i] and s2[i] != s3[i]):
            flag = True
            print("YES")
            break
    if not flag:
        print("NO")
    