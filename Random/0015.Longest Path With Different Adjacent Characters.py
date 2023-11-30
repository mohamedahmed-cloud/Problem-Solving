#    Author : Mohamed Yousef 
#    Date   : 2023-01-13
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution():
    def solve(self,parent,s):
        tree=defaultdict(list)
        for i,value in enumerate(parent):
            tree[value].append(i)
        ans=1
        def dfs(node):
            nonlocal ans
            m1,m2=0,0
            for i in tree[node]:
                nextNode=dfs(i)
                if s[i]!=s[node]:
                    if nextNode>m1:
                        m2=m1
                        m1=nextNode
                    elif nextNode>m2:
                        m2=nextNode
            ans=max(ans,m1+m2+1)
            return m1+1
        dfs(0)
        return ans

solve=Solution()
print(solve.solve([-1,0,0,0],"aabc"))