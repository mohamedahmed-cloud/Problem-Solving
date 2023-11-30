import math
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(fx - sx)
        height = abs(fy - sy)
        if width == 0 and height == 0 and t == 1: 
            return False
        return max(width, height) <= t

slv = Solution()
sx = 1
sy = 3
fx = 1
fy = 1
t = 2
print(slv.isReachableAtTime(sx, sy, fx, fy, t))
