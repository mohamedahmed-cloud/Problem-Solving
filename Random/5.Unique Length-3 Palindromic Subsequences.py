#    Author : Mohamed Yousef 
#    Date   : 2023-05-06
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,s):
        main = [[-1 for i in range(2)] for j in range(26)]
        n = len(s)
        ans = 0

        for i in range(n):
            if main[ord(s[i]) - ord('a')][0] == -1:
                main[ord(s[i]) - ord('a')][0] = i
            else:
                main[ord(s[i]) - ord('a')][1] = i
                
        # print(main)
        
        for i in range(26):
            freq = [0] * 26
            for j in range(main[i][0] + 1, main[i][1]):
                if freq[ord(s[j]) - ord("a")] == 0:
                    # print(s[main[i][0]],s[j],s[main[i][1]])
                    ans += 1
                freq[ord(s[j]) - ord("a")] = 1
            
        return (ans)

solve=Solution()
print(solve.solve("bbcbaba"))