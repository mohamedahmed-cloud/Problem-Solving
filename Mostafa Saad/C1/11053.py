#    Author : Mohamed Yousef 
#    Date   : 2023-05-05
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

try:
    while True:
        N, a, b = mvalues()
        visited = defaultdict(int)
        x = 0
        survive = N
        number = (a * x **2 + b) % N
        while True:
            visited[number] += 1
            if visited[number] == 2:
                survive -= 1
            if visited[number] == 3:
                break
            number = (a * number * number + b) % N
        print(survive)
        # print(visited)
except:
    pass    