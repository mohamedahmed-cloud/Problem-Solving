class Solution:
    def solve(self,s):
        open = 0
        close = 0
        for i in s:
            if i == "[":
                open += 1
            elif i == "]":
                if open == 0:
                    close += 1
                else:
                    open -= 1
        return (close + 1) // 2



solve=Solution()    
print(solve.solve( "]]][[["))