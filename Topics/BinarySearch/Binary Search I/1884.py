class Solution:
    def twoEggDrop(self, n: int) -> int:
        x = 0
        res = 0
        while res < n:
            x += 1
            res = x * (x + 1) // 2

        return x