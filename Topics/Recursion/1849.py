class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def dfs(indx, prev):
            if indx == n : return True
            
            for i in range(indx, n):
                val = int(s[indx: i + 1])
                if val == prev - 1 and dfs(i + 1, val):
                    return True



        for i in  range(n - 1):
            val = int(s[:i + 1])
            if dfs(i + 1, val):return True
            
        return False
    
slv = Solution()
print(slv.splitString("421"))