from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict(list)
        for win, lose in matches:
            if not cnt[win]:
                cnt[win] = [0, 0]
            if not cnt[lose]:
                cnt[lose] = [0, 0]
            cnt[win] = [cnt[win][0] + 1, cnt[win][1]]
            cnt[lose] = [cnt[lose][0], cnt[lose][1] + 1]
        # print(cnt)
        ans = [[], []]
        for key, val in cnt.items():
            if val[1] == 0:
                ans[0].append(key)
            elif val[1] == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans
slv = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(slv.findWinners(matches))


            