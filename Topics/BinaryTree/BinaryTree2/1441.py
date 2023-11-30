from typing import Optional, List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        our_set = set(target)
        for i in range(1, max(target) + 1):
            stack.append("Push")
            if i not in our_set:
                stack.append("Pop")
        return stack

slv = Solution()
target = [1,3]
n = 3
print(slv.buildArray(target, n))

