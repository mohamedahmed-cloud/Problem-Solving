#    Author : Mohamed Yousef 
#    Date   : 2024-01-06
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

def solve():
    n = test()
    l = lvalues()
    save = [0]
    cnt = 0
    
    for i in range(n):
        if  (i & 1): l[i] *= -1
        cnt += l[i]
        save.append(cnt)
    save.sort()
    
    for i in range(1, n + 1):
        if i == 0 or save[i] == save[i - 1]:
            return "YES"
    return "NO"


for _ in range(test()):
    print(solve())    
