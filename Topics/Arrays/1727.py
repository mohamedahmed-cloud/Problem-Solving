#!/usr/bin/python3

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(col):
            for j in range(1, row):
                if matrix[j][i] != 0:
                    matrix[j][i] += matrix[j - 1][i]
        mx = 0
        for i in matrix:
            curr_min = float("inf")
            i.sort(reverse=True)
            sequence = 1
            for j in i:
                if curr_min > j:
                    curr_min = j
                res = sequence * curr_min
                if j == 0:
                    sequence = 1
                else:
                    sequence += 1
                # print(sequence)
                if mx < res:
                    mx = res
        return mx

slv = Solution()
matrix = [[0,0,1],[1,1,1],[1,0,1]]
print(slv.largestSubmatrix(matrix))