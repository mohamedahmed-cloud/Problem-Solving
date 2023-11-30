class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
       
        if n == 1: return 0

        def find(n, k):
            
            if n == 2: return k - 1
            half = 1 << (n -2)

            if half >= k:
               return find(n-1, k)
            
            else:
               
               return int(not find(n-1, k - half ))
            
        return find(n, k)


slv = Solution()
print(slv.kthGrammar(3,4))