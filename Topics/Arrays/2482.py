from typing import List
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        rows = []
        cols = []
        for row in grid:
            tmp = sum(row)
            rows.append([tmp, m - tmp])

        for i in range(m):
            tmp = 0
            for j in range(n):
                tmp += grid[j][i]
            cols.append([tmp, n - tmp])
        print(rows, cols)
        ans = []

        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(rows[i][0] + cols[j][0] - rows[i][1] - cols[j][1])
            ans.append(tmp)
        # print(ans)
        return ans


from itertools import product
# another Excellent Solution
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        def count(nums): return 2 * sum(nums) - len(nums)

        rows = list(map(count, grid))
        cols = list(map(count, zip(*grid)))
        for i, j in product(range(n), range(m)):
            grid[i][j] = rows[i] + cols[j]
        return grid

slv = Solution()
grid = [[0,1,1],[1,0,1],[0,0,1]]
print(slv.onesMinusZeros(grid))
