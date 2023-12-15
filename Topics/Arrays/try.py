from typing import List
from itertools import product

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        def count(nums) : return 2*sum(nums)-len(nums)       # [1] count score for a list of numbers
            
        rows = list(map(count, grid))                        # [2] count scores for rows
        cols = list(map(count, zip(*grid)))                 # [3] count scores for columns (transpose)
        print(rows, cols)

        for i,j in product(range(m), range(n)):              # [4] update the input matrix with
            grid[i][j] = rows[i] + cols[j]                   #     sums of precomputed scores
                
        return grid

slv = Solution()
grid = [[0,1,1],[1,0,1],[0,0,1]]
print(slv.onesMinusZeros(grid))