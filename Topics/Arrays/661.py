from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                count = 0
                cnt = 0
                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(m, j + 2)):
                        count += img[x][y]
                        cnt += 1
                ans[i][j] = (count // (cnt))
        return ans
    
slv = Solution()
slv.imageSmoother([[100,200,100],[200,50,200],[100,200,100]])
