#    Author : Mohamed Yousef 
#    Date   : 2023-01-15
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        l=[]
        n=len(s1)
        for i in range(n):
            l.append({s1[i],s2[i]})
        iter=0
        for i in range(iter,n):
            for k in l[i]:
                check=False
                for j in range(iter+1,n):
                    if k in l[j]:
                        l[j]|=l[i]
                        l[i]={1}
                        check=True
                        break
                if check:break
            iter+=1
        ans=""
        # check=True
        for i in baseStr:
            check=True
            for j in l:
                if i in j:
                    check=False
                    ans+=min(min(j),i)
            if check:
                ans+=i
        return ans,l

solution=Solution()
print(solution.smallestEquivalentString("leetcode","programs","sourcecode"))
