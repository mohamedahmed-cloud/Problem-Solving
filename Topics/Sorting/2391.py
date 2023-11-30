from collections import defaultdict
from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # prefix sum 
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        ans = 0
        n = len(garbage)
        d_dict =  {i: {"M":0, "G":0, "P":0}  for i in range(n)}
        curr = 0
        for i in garbage:
            for j in i:
                d_dict[curr][j] += 1
            curr += 1
        print(d_dict)

        # last M, G, P
        last = {"M":-1, "G":-1, "P":-1}
        for key, value in d_dict.items():
            x = 0
            for i, j in value.items():
                ans += j
                if j != 0:
                    last[i] = key

        for key, value in last.items():
            if value - 1 >= 0:
                print(ans)
                ans += travel[value - 1]
        return ans


slv = Solution()
garbage = ["MMM","PGM","GP"]
travel = [3,10]
print(slv.garbageCollection(garbage, travel))
