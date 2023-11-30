#    Author : Mohamed Yousef 
#    Date   : 2023-02-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,s,numRows):
        # A very tought day.
        n=len(s)
        print(n)
        if numRows==1:return numRows
        step=(numRows-1)*2
        ans=""
        for i in range(numRows):
            inner=(numRows-1)*2-2*i
            for j in range(i,n,step):
                ans+=s[j]
                if i>0 and i<numRows-1:
                    if inner+j<n:
                        ans+=s[inner+j]
        return ans
solve=Solution()
print(solve.solve("PAYPALISHIRING",3))

