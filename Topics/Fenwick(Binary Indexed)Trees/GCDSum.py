#    Author : Mohamed Yousef 
#    Date   : 2024-01-01

from sympy.ntheory import totient, divisors
from random import sample
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(str,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


# To find the children

def query(BITTree,start, end): 
	s = 0
	end += 1

	while end > start: 
		s += BITTree[end] 
		# 2's complement then & with orignal then - => to find child
		end -= end & (-end) 
	return s 

# tree, length of tree, index, value for this index
def update(BITTree , n , indx ,val): 
	indx += 1
	while indx <= n: 
		BITTree[indx] += val
		# 2's complement then & with orignal then + => to find parent
		indx += indx & (-indx) 

# to construct the tree
def construct(arr, n): 
	BITTree = [0]*(n+1)
	for i in range(n): 
		update(BITTree, n, i, arr[i]) 

	return BITTree 

def pillai(n):
    return sum([n*totient(d)//d for d in divisors(n)])

n = test()
l = lvalues()
freq = []
for i in l:
    freq.append(pillai(i))


# build the tree.
BITTree = construct(freq, n)

q = test()
for i in range(q):
	s, start, end = mvalues()
	start, end = int(start), int(end)
	
	if s == "C":
		print(query(BITTree,start - 1, end  - 1))
	elif s == "U":
		update(BITTree, n, start - 1, end - 1)













