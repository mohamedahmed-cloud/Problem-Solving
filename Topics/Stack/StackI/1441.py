from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ans = []
        indx = 0
        x = len(target) - 1

        for i in range(1, n + 1):
            stack.append("Push")
            ans.append(i)

            if ans[-1] != target[indx]:
                stack.append("Pop")
                ans.pop()

            elif x - indx:
                indx += 1
                
            else:
                return stack

        return stack


# another faster solution.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        newTarget = set(target)
        stack = []

        for i in range(1, max(target) + 1):
            
            if i in newTarget:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")

        return stack
