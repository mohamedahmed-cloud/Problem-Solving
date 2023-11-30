#    Author : Mohamed Yousef 
#    Date   : 2023-02-02
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,words,order):
        Dict=defaultdict(str)
        iter=0
        n=len(words)
        for i in order:
            Dict[i]=iter
            iter+=1
        Dict["0"]=-1
        for i in range(n):
            words[i]+="0"*(20-len(words[i]))
        for i in range(20):
            j=0
            iter=1
            for j in range(n-1):
                if Dict.get(words[j][i])<Dict.get(words[j+1][i]):
                    iter+=1
                elif Dict.get(words[j][i])==Dict.get(words[j+1][i]):
                    iter+=1e3
                else:return False
                if iter==n:return True
        return True


solve=Solution()
print(solve.solve(["apple","apple","app"],"abcdefghijklmnopqrstuvwxyz"))