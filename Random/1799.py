import math
class Solution:
    def solve(self, nums):
        nums.sort()
        double = []
        n = len(nums)
        b =2
        for i in range(n - 1,-1,-1):
            curr = n - b
            b += 1

            while curr >= 0:
                if nums[curr] != "prevent" and nums[i] != "prevent" and nums[i] % nums[curr] == 0 and nums[curr] != 1 :
                    x = [nums[i], nums[curr]]
                    double.append(x)
                    nums[curr] = "prevent"
                    nums[i] = "prevent"
                    break
                curr -= 1
            # print(nums)

        temp = []
        for i in nums:
            if i != "prevent":
                temp.append(i)
        ans = 0
        
        x = len(temp) // 2
        curr = x + 1
        double.sort()
        print(double)
        for i in double:
            ans += (curr) * i[1]
            curr += 1

        return ans



solve=Solution()
print(solve.solve([1,2,3,4,5,6]))


