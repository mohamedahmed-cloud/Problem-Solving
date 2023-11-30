from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        # backtrack(n, ans + "0")
        # backtrack(n, ans + "1")
                0
        00              01
    000     001       010   011
        
        
        """
        n = len(nums[0])
        token = set(nums)
        

        def backtrack(indx, ans):
            if indx == 0:
                print(ans)

                if  ans not in token:
                    return ans
                return ""
            start_with_zero = backtrack(indx - 1, ans + "0")
            
            if start_with_zero:
                return start_with_zero

            return backtrack(indx - 1, ans + "1")

        return backtrack(n, "")




slv = Solution()
l = ["000", "001", "011"]
print(slv.findDifferentBinaryString(l))