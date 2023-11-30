#    Author : Mohamed Yousef 
#    Date   : 2023-02-05
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
class Solution:
    def solve(self,mat,r,c):
        ans=[]
        out=[]
        store=[]
        for i in mat:
            out.extend(i)
        n=len(out)
        if n==(r*c):
            for i in range(n):
                store.append(out[i])
                if (i+1)%c==0:
                    ans.append(store)
                    
                    store=[]
            return ans
        return mat
                
        
solve=Solution()
print(solve.solve([[1,2]],1,2))

class Solution:
    def solve(self,mat,r,c):
        n=len(mat)
        m=len(mat[0])
        if r*c!=m*n:return mat
        ans=[[0 for x in range(c)] for y in range(r)]
        for i in range(r*c):
            ans[i//c][i%c]=mat[i//m][i%m]
        return ans




solve=Solution()
print(solve.solve([[1,2],[3,4]],1,4))