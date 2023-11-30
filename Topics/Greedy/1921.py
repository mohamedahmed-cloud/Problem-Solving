from typing import Optional, List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        n = len(dist)

        for i in range(n):
            time.append(round(dist[i] / speed[i], 7))
        time.sort()

        curr_time = 0
        for i in range( n):
            if time[i] <= curr_time:
                break
            curr_time += 1

        return curr_time

slv = Solution()
dist = [4,2,3]
speed = [2,1,1]
print(slv.eliminateMaximum(dist, speed))