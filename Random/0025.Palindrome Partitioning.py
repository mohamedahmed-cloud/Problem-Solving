#    Author : Mohamed Yousef 
#    Date   : 2023-01-22
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(500) #To increase Recursion depth in py

class Solution:
    def solve(self,s):
        def check(string):
            return string==string[::-1]
        def backTrack(start,currentPartitions,ans):
            if start==len(s):
                ans.append(currentPartitions)
                # print(ans)
                return 
            for i in range(start,len(s)):
                if check(s[start:i+1]):
                    backTrack(i+1,currentPartitions+[s[start:i+1]],ans)
                    # print(ans)
        ans=[]
        backTrack(0,[],ans)
        return ans



solve=Solution()
print(solve.solve("xxxxxxxxxxx"))