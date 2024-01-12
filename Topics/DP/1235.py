
from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(jobs)
        print(jobs)
        dp = [0] * (n + 1)
        for i, (e, s, p) in enumerate(jobs):
            indx = bisect_right(jobs, s, key = lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[indx] + p)
            print(dp, indx, dp[indx], s)
        print(dp)
        return dp[n]
    


slv = Solution()
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(slv.jobScheduling(startTime, endTime, profit))
