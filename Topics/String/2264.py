class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        mx = -float("inf")
        n = len(num)
        for i in range(2, n):
            if num[i - 1] == num[i - 2]  == num[i]:
                if not ans or (ans and mx < int(num[i])):
                    mx = int(num[i])
                    ans = num[i] * 3
        return ans
    
slv = Solution()
num = "6777133339"
print(slv.largestGoodInteger(num))

