#    Author : Mohamed Yousef 
#    Date   : 2023-12-18
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


def main():
    
        x = svalues()
        curr = 0
        n = len(x)
        # print(x)
        for curr in range(1, n):
            n1 = int(x[:curr])
            n2 = int(x[curr:])
            if n1 < n2 and len(str(n1)) + len(str(n2)) == n:
                return [x[:curr], x[curr:]]
        return [-1]
for i in range(test()):
    ans = (main())
    print(*ans)