from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        ans = 0
        def dfs(str1,str2, indx):
            nonlocal ans

            if len(str1) == len(set(str1)):
                ans = max(ans, len(str1))
            else:
                return
            if len(str2) == len(set(str2)):
                ans = max(ans, len(str2))
            else:
                return 
                
            for i in range(indx, n):
                dfs(str1 + arr[i],str1, i + 1)
            
        dfs("","", 0)
        return ans
slv = Solution()
arr =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
print(slv.maxLength(arr))
