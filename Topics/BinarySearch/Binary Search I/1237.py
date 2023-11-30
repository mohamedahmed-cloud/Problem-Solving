
#    This is the custom function interface.
#    You should not implement it, or speculate about its implementation
from typing import Optional, List

class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass
    
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        ans = []

        loop = 1000
        for x in range(1, 1001):
            for y in range(loop, 0, -1):
                if customfunction.f(x,y) <= z:
                    loop = y
                    break
                    
            if customfunction.f(x,y) == z:
                ans.append([x,y])

        return ans

        