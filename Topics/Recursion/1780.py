class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans = set()
        temp = 3
        def find(n):
            nonlocal temp

            if n == 0 : return True
            if n < 0 : return False

            i = 0
            while n >= temp ** i:
                temp = 3
                i += 1

            temp = temp ** (i -1)

            if temp in ans: return False

            ans.add(temp)
            return find(n - temp)
        
        return find(n)
