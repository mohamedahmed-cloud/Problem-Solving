#    Author : Mohamed Yousef 
#    Date   : 2023-01-21
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
# You must review this problem again
class Solution:
    def solve(self,s):
        res = []
        def BT(i,address):
            if i==len(s):
                if len(address)==4:
                    # print(address)
                    res.append( '.'.join(map(str,address)) )
                return
            if address[-1]!=0 and address[-1]*10+int(s[i]) <= 255:
                lastItem = address[-1]
                address[-1] = lastItem*10+int(s[i])
                BT(i+1, address)
                address[-1] = lastItem
            
            if len(address)<4:
                BT(i+1,address + [int(s[i])])
        
        BT(1,[int(s[0])])
        return res

        



solve=Solution()
print(solve.solve("25525511135"))