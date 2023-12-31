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
def query(BITTree, end, indx): 
	s = 0
	while end > 0:
		# print(end, indx)
		s += BITTree[end][indx]
		# 2's complement then & with orignal then - => to find child
		end -= end & (-end) 
	return s 

# tree, length of tree, index, value for this index
def update(BITTree , n , indx ,val):
	indx += 1
	while indx <= n:
		tmp = [0, 0]
		if val & 1:
			tmp[1] = 1
		else: tmp[0] = 1

		BITTree[indx] = [BITTree[indx][0] + tmp[0], BITTree[indx][1] + tmp[1]]

		# 2's complement then & with orignal then + => to find parent
		indx += indx & (-indx) 

# to construct the tree
def construct(arr, n): 
	BITTree = [[0, 0]]*(n+1)
	for i in range(n): 
		update(BITTree, n, i, arr[i]) 
	# print(BITTree)
	return BITTree 


# Driver code to test above methods 
n = test()
l = lvalues()
BITTree = construct(l,n) 


for i in range(test()):
	a, b, c = mvalues()
	if a == 0:
		update(BITTree, n, b, c)
	else:
		print(query(BITTree,c, a - 1) - query(BITTree,b - 1 , a -1))



