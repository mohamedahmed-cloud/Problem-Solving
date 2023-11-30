from typing import Optional, List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        ans = [0] * (2 * n -1)
        size = 2 * n -1

        def find(seen, i):
            nonlocal n, size

            if len(seen) >= n or i >= size: return True

            if ans[i]:return find(seen, i + 1)

            for num in range(n, 0, -1):
                if num in seen:continue
                elif num + i >= size and num != 1: continue
                elif num != 1 and ans[i + num]:continue

                ans[i] = num
                if num != 1: ans[num + i] = num
                seen.add(num)

                res = find(seen, i + 1) 
                if res:return True
                elif num != 1: ans[i + num] = 0
                ans[i] = 0

                seen.remove(num)
            # return False
        
        find(set(), 0)
        return ans

slv = Solution()
print(slv.constructDistancedSequence(6))