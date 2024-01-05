#    Author : Mohamed Yousef 
#    Date   : 2023-12-28
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


def isPerfectSquare(n):
    if n <= 1:
        return True
 
    left, right = 1, n
 
    while left <= right:
        mid = left + (right - left) // 2
 
        square = mid * mid
 
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
 
    return False

for _ in range(test()):
    n = test()
    x = sum(lvalues())  
    if isPerfectSquare(x):
        print("YES")
    else:
        print("NO")