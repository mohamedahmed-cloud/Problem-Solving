class Solution:
    def numDecodings(self, s: str) -> int:
        prepare = []
        n = len(s)
        add = s[0]
        if add == "0": return 0
        for i in range(1,n):
            if s[i] != "0":
                prepare.append(add)
                add = s[i]
            else:
                add += s[i]
                if int(add) > 26:
                    return 0

        prepare.append(add)
        n = len(prepare)
        add = ""
        ans = 1
        x = 0
        for i in range(1, n):
            add = prepare[i - 1] + prepare[i]
            if int(add) <= 26:
                x += 1
        x += x  - 1
        return ans + x

slv = Solution()
s = "1122"
print(slv.numDecodings(s))