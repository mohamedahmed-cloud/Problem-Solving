from typing import Optional, List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = ans = []
        dic = {}

        for i in nums2:
            while stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)

        while stack:
            dic[stack.pop()] = -1

        # print(dic)
        for i in nums1:
            ans.append(dic[i])
        return ans

slv = Solution()
x = slv.nextGreaterElement([4,1,2], [1,2,4])
print(x)