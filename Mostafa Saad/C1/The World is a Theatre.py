#    Author : Mohamed Yousef 
#    Date   : 2023-05-01
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

boy, girl, team = mvalues()
curr = 4
ans = 0

while curr + girl < team:
    curr +=1

for i in range(curr, team):
    if team - i < 1: break
    ans += math.comb(boy, i)*math.comb(girl, team - i)

print(ans)
