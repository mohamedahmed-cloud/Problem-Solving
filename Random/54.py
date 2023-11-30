class Solution:
    def solve(self, matrix):
        left = 0
        right = cols  = len(matrix[0]) - 1
        top = 0
        bottom = rows = len(matrix) - 1
        curr = 0
        ans = []

        while len(ans) < (cols + 1 ) * (rows + 1) :
            if top <= rows:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1

            
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if bottom >= top:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

     

            curr += 1
            # print(ans)
        return ans


solve=Solution()
print(solve.solve([[2,5,8],
                   [4,0,-1]]))
# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
# [[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]]