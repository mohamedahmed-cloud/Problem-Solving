#    Author : Mohamed Yousef 
#    Date   : 2023-02-10
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
def twoD(x): return [[ 0 for i in range(x)] for j in range(x)]
class Solution:
    def solve(self,grid):
        n=len(grid)
        def check(newArray,n):
            isZero=0
            allZero=0
            import copy
            oldArray=copy.deepcopy(newArray)
            for i in range(n):
                for j in range(n):
                    if oldArray[i][j]==1:
                        isZero+=1
                        # print(newArray)
                        try:newArray[i+1][j]=1
                        except:pass
                        try:
                            if i-1>=0: 
                                newArray[i-1][j]=1
                        except:pass
                        try:newArray[i][j+1]=1
                        except:pass
                        try:
                            if j-1>=0:
                                newArray[i][j-1]=1
                        except:pass
                    else:
                        allZero+=1
            return newArray ,isZero,allZero
        x=-1
        l=check(grid,n)
        while l[1]!=n*n:
            x=max(0,x)
            l=check(l[0],n)
            x+=1
            if l[2]==n*n:
                return -1
        return x



solve=Solution()
print(solve.solve([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))