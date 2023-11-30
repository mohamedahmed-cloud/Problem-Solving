#    Author : Mohamed Yousef 
#    Date   : 2023-06-24
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

def solve ():
    n, x = mvalues()
    s1 = lvalues()
    s2 = lvalues()
    s3 = lvalues()
    res = 0
    for i in s1:
        # check if bit in the x or not 
        if i & x != i:
            break
        res |= i
    for i in s2:
        # check if bit in the x or not 
        if i & x != i:
            break
        res |= i
    for i in s3:
        # check if bit in the x or not 
        if i & x != i:
            break
        res |= i
    return "Yes" if res == x else "NO"

if __name__ == '__main__':
    for i in range(test()):
        res = solve()
        print(res)