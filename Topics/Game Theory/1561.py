from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        ans = 0
        print(piles)
        for i in range(n//3, n, 2):
            ans += piles[i]
        return ans


slv = Solution()
piles = [9,8,7,6,5,1,2,3,4]
print(slv.maxCoins(piles))