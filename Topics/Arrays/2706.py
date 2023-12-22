    from typing import List

    class Solution:
        def buyChoco(self, prices: List[int], money: int) -> int:
            mn = [float("inf"), 0]
            for i, val in enumerate(prices):
                if mn[0] > val:
                    mn = [val, i]

            mn2 = float("inf")
            for i, val in enumerate(prices):
                if mn2 > val and i != mn[1]:
                    mn2 = val
            ans = money - (mn[0] + mn2)
            return  ans if ans >= 0 else money  

    slv = Solution()
    prices = [1,2,2]
    money = 3
    slv.buyChoco(prices, money)