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

with open("pails.in") as f:
    x, y, m = f.readline().split()
x, y, m = int(x), int(y), int(m)
mod = m // y
constant = y * mod
print(constant)
stop = m // x
print(stop)
x1 = 0
y1 = 0

mx = constant
while y1 <=  stop and constant - y * y1 >= 0:
    while constant - y * y1 + x1 * x <= m:
        tmp = constant - y * y1 + x1 * x
        if tmp > mx: mx = tmp 
        x1 += 1
    y1 += 1

print(x1, y1)
print(mx, file=open("pails.out", "w"))



