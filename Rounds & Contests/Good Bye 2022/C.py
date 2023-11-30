#    Author : Mohamed Yousef 
#    Date   : 2023-06-26

import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

def generatePrime():
    prime = [True for i in range(102)]
    prime[0] =  prime[1]  = False
    for i in range(2, 102):
        if prime[i]:
            for j in range(i * i, 102, i):
                prime[j] = False
    ans = []
    for i in range(102):
        if prime[i]:
            ans.append(i)
    return ans  
                
for _ in range(test()):
    n = test()
    l = lvalues()
    prime = generatePrime()
    if len(l) != len({*l}):
        print("NO")
        continue
    else:
        flag = True
        for p in prime:
            freq = [0] * (p )
            for i in l:
                freq[i % p] += 1
            if min(freq) > 1:
                flag = False
    if flag:
        print("YES")
        continue
    print("NO")
