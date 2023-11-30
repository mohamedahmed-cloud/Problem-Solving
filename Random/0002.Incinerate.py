#    Author : Mohamed Yousef 
#    Date   : 2022-12-19
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
t = int(input())
for _ in range(t):
	n,k = map(int,input().split())
	h = list(map(int,input().split()))
	p = list(map(int,input().split()))
	z = list(sorted(zip(p,h)))
	M = max(h)
	tot = k
	i = 0
	while i<n and M>0 and k>0:
		if z[i][1]>tot:
			k=max(0,k-z[i][0])
			tot+=k
		else:
			i+=1
	# print(M)
	if M>tot:
		print("NO")
	else:print("YES")
