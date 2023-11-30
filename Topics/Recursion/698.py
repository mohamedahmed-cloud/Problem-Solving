from typing import Optional, List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        summation = sum(nums)
        if summation % k: return False

        n = len(nums)
        target = summation // k
        track = [False] * n
        nums.sort(reverse=True)

        def backtrack(i, subSum, k):
            nonlocal n, target
            if k == 0: return True
            
            if subSum == target:return backtrack(0, 0, k-1)
            # print(subSum)
            for j in range(i, n):
                if track[j] or nums[j] + subSum > target:continue
                if j != 0 and not track[j -1] and nums[j-1] == nums[j]:
                    continue
                track[j] = True
                if backtrack(j + 1, subSum + nums[j], k):return True

                track[j] = False
                
            return False
        
        return backtrack(0, 0, k)




slv = Solution()
print(slv.canPartitionKSubsets([4,3,2,3,5,2,1], 4))

slv = Solution()
print(slv.canPartitionKSubsets([10,5,5,4,3,6,6,7,6,8,6,3,4,5,3,7], 8))
        


