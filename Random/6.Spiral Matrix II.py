class Solution:
    def solve(self, n):
        top = 0
        left = 0
        right = n - 1
        bottom = n - 1
        ans = [[-1 for i in range(n)] for j in range(n)]
        count = 1

        while count <= n * n:

            for i in range(left, right + 1):
                ans[top][i] = count 
                count += 1
            top += 1

            for i in range(top , bottom + 1):
                ans[i][right] = count
                count += 1
            right -= 1

            if bottom >= top:
                for i in range(right, left - 1, -1):
                    ans[bottom ][i] = count
                    count += 1
                bottom -= 1
            # break

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans[i][left] = count
                    count += 1
                left += 1

            # print(ans, count)
        return ans

solve=Solution()
print(solve.solve(4))
