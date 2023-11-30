#    Author : Mohamed Yousef 
#    Date   : 2023-05-07
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

n = float(input())
while n != 0:
    a = math.floor(math.pow(n, 1 / 3) + 1e-6)
    # print(a)
    dx = (n - a ** 3) / (3 * a ** 2)
    
    print(f'{dx + a:.4f}')
    n = float(input())
