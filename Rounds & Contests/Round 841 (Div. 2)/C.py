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

def perfectSquare():
    return [i * i for i in range(600)]

def solve():
    n = test()
    l = lvalues()

    # ans = total number of sub array - number of sub array that have odd divisor.
    # ans = n * (n + 1 ) // 2 - number that has perfect square xor

    pfx = list(accumulate(l, lambda i,y : i ^ y))

    count = [0] * (2 * n + 1)
    count[0] = 1
    square = perfectSquare()
    ans = n * (n + 1) // 2

    for i in range(len(l)):
        for j in square:
            if j >= 2 * n:break
            # try:
            if pfx[i] ^ j < 2 * n: ans -= count[pfx[i] ^ j]

        count[pfx[i]] += 1


    print(ans)


if __name__ == '__main__':
    for i in range(test()):
        solve()