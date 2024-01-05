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

for _ in range(test()):

    for i in range(3):
        x = svalues()
        if "?" in x:
            save = list(x)
    l = {"A": 0, "B":0, "C":0}
    for i in save:
        if i != "?":
            l[i] += 1
    for i, val in l.items():
        if val == 0:
            print(i)



    
        
    
    