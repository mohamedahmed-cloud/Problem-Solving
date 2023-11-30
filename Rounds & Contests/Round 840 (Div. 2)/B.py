#    Author : Mohamed Yousef 
#    Date   : 2023-06-22
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

t = test()
for _ in range(t):
	n,k = mvalues()
	h = lvalues()
	p = lvalues()
	Max = max(h)
	ph = sorted(zip(p,h))
	tot = k
	i = 0
	n = len(ph)
	while i < n and k != 0:
		if tot < ph[i][1]:
			k = max(0, k - ph[i][0])
			tot += k
		else:
			i += 1
	if tot >=  Max:
		print("YES")
	else:
		print("NO") 		 		  	  	  			

    
    
