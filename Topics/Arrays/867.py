from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        for j in range(m):
            tmp = []
            for i in range(n):
                tmp.append(matrix[i][j])
            ans.append(tmp)

        return matrix
slv = Solution()
matrix = [[1,2,3],[4,5,6]]
slv.transpose(matrix)