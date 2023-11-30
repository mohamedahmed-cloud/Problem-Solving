
# if i > 0 and not visited[i -1] and nums[i] == nums[i - 1]:
#       continue


# Hope this helps


# Full Code:
from typing import Optional, List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
            
            n = len(nums)
            nums.sort(reverse=True)
            total = sum(nums)
            if total % k != 0:
                return False
            
            target = int(total / k)
            used = [False] * n
            
            def dfs(index, total, k): 
                
                if k == 0:
                    return True
                
                if total == 0:
                    return dfs(0, target, k - 1)
                
                for i in range(index, n):
                    
                    if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                        continue
                        
                    if used[i] or total - nums[i] < 0:
                        continue
                    
                    used[i] = True
                    if dfs(i + 1, total - nums[i], k):
                        return True
                    used[i] = False
                return False
            
            return dfs(0, target, k)


slv = Solution()
print(slv.canPartitionKSubsets([4,3,2,3,5,2,1], 4))

slv = Solution()
print(slv.canPartitionKSubsets([10,5,5,4,3,6,6,7,6,8,6,3,4,5,3,7], 8))