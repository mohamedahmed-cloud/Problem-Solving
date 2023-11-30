from typing import Optional, List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        res = []
        def backtrack(ans, i):
            print(ans)
            nonlocal n, k

            if len(ans) >= n:
                res.append(int(ans))
                return
            for j in range(10):
                if i == 0 or abs(int(ans[-1]) - j) == k:
                    backtrack(ans + str(j), i + 1)
            
        
        for i in range(1, 10):
            backtrack(str(i), 1)
        return res

slv = Solution()
print(slv.numsSameConsecDiff(3, 7))