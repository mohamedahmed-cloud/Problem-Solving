#    Author : Mohamed Yousef 
#    Date   : 2023-01-27
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,words):
        ans=[]
        wordSet=set(words)
        def dfs(word):
            n=len(word)
            for i in range(1,n):
                prefix=word[:i]
                suffix=word[i:]
                if (prefix in wordSet and suffix in wordSet) or \
                    (prefix in wordSet and dfs(suffix)):
                    return True
        for i in words:
            if dfs(i):
                ans.append(i)
        return ans




solve=Solution()
print(solve.solve(["cat","dog","catdogcat"]))