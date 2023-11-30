class Solution:
    def solve(self, mat):
        n = len(mat)
        ans = 0

        for i in range(n):
            for j in range(n):
                if i == j :
                    ans += mat[i][j]
                elif i + j + 1 == n:
                    ans += mat[i][j]
        return ans

        
solve=Solution()
print(solve.solve([[5]]))

class Solution:
    def solve(self, mat):
        n = len(mat)
        ans = 0

        for i in range(n):
            ans += (mat[i][i] + mat[i][-1 - i])
        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]
        return (ans)


solve=Solution()
print(solve.solve([[7]]))
# -3 [[-3,-2, -1]
# -2 [-3, -2, -1] 
# -1 [-3, -2, -1]]
