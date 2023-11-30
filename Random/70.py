class Solution:
    def solve(self, n ):
        memo = {}
        def fib(n):
            if n <= 2: return n
            if n in memo:
                return memo[n]
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        return fib(n)


solve=Solution()
print(solve.solve(90))