from typing import Optional, List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        ans = 0
        stack = [float('inf')]
        for i in arr:
            while stack[-1] <= i:
                last = stack.pop()
                ans += last * min(stack[-1], i)
            stack.append(i)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
            
        return ans

    
slv = Solution()
print(slv.mctFromLeafValues([18,13,5,3,15]))