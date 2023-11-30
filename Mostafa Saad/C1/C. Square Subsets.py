#    Author : Mohamed Yousef 
#    Date   : 2023-06-25
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

def perfectSquare():
    ans = []
    for i in range(1,72):
        ans.append(i * i)
    return ans

square = perfectSquare()
mod = 10 ** 9 + 7
n = test()
l = lvalues()
ways = n * (n + 1) // 2  - 1
count = [0] * (2 * 70 * 70 + 1)
count[0] = 1
t = 0
for i in l:
    t ^= i
    for j in square:
        ways -= count[ t ^ j]
    count[t] += 1
print(ways)

