from typing import Optional, List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = deque([0] * n)
        stack = deque([(0, temperatures[0])])

        for i in range(1, n):
            while stack and stack[-1][1] < temperatures[i] :
                ans[stack[-1][0]] = (i -  stack[-1][0])
                stack.pop()
               
            stack.append((i, temperatures[i]))

      
        while len(stack) >= 2:
            if stack[-1][1] > stack[-2][1]:
                ans[stack[-2][0]] =  stack[-1][0] - stack[-2][0] 
            stack.pop()
        
        # ans = [0 if x == float("inf") else x for x in ans]
        
        return ans



slv = Solution()
print(slv.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))