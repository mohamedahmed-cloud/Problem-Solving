class Solution:
    def solve(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        l = [[0 for i in range(n + 1)] for j in range(m + 1)]
        nums1.insert(0, -100)
        nums2.insert(0, -101)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums2[i] == nums1[j]:
                    l[i][j] = 1 + l[i - 1][j - 1]
                else:
                    l[i][j] = max(l[i - 1][j] , l[i][j - 1])
        # print(l)
        return l[m][n]

solve=Solution()
print(solve.solve([1,3,7,1,7,5],  [1,9,2,5,1]))