from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ans = 0

        def calculate(row, col):
            cnt = 0
            for i in range(m):
                if mat[row][i] == 1:
                    cnt += 1
            for i in range(n):
                if mat[i][col] == 1:
                    cnt += 1
            # print("cnt",cnt)
            return cnt <= 2

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    ans += calculate(i, j)
                    continue
        # print(ans)
        return ans
    

slv = Solution()
mat = mat = [[0,1,0],[1,0,0],[0,0,1]]
print(slv.numSpecial(mat))

