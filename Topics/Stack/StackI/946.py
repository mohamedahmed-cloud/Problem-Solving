from typing import Optional, List
from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque([])
        popped = deque(popped)
        popped.reverse()
        pushed = deque(pushed)

        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()

        return not stack
    

# slv = Solution()
# print(slv.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))