#    Author : Mohamed Yousef 
#    Date   : 2024-01-01
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

# To find the children
def query(BITTree, end): 
	s = 0
	while end > 0:
		s += BITTree[end]
		end -= end & (-end)

	return s 

# tree, length of tree, index, value for this index
def update(BITTree , n , indx ,val):
	while indx <= n:
		BITTree[indx] += (val & 1)
		indx += indx & (-indx) 

def update2(BITTree , n , indx ,val):
	tmp = 0
	if (l[indx - 1] & 1 )and not val & 1:
		tmp = -1
	if (not l[indx - 1] & 1) and (val & 1):
		tmp = 1
	l[indx - 1] = val
	while indx <= n:
		BITTree[indx] += tmp
		indx += indx & (-indx) 


# to construct the tree
def construct(arr, n): 
	BITTree = [0]*(n+1)
	for i in range( n): 
		update(BITTree, n, i + 1, arr[i]) 
	# print(BITTree)
	return BITTree 


# Driver code to test above methods 
n = test()
l = lvalues()
BITTree = construct(l,n) 


for i in range(test()):
	a, b, c = mvalues()
	if a == 0:
		# print(BITTree)
		update2(BITTree, n, b, c)
		# print(BITTree)
	elif a == 2:
		tmp = query(BITTree, c) - query(BITTree, b - 1)
		print(tmp)
	elif a == 1:
		tmp = query(BITTree,c) - query(BITTree, b - 1)
		print(c - b + 1 - tmp)

