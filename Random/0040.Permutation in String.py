#    Author : Mohamed Yousef 
#    Date   : 2023-02-04
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()

class Solution:
    def solve(self,s1,s2):
        n=len(s2)
        m=len(s1)
        store=defaultdict(int)
        for i in s1:
            store[i]+=1
        # print(store)
        for i in range(0,n):
            store2=defaultdict(int)
            for j in range(i,min(i+m,n)):
                store2[s2[j]]+=1
            print(store2)
            if store==store2:
                return True
        return False
                
solve=Solution()
print(solve.solve("ab","eidboaoo"))

# Second solution
# When you compare any thing with each other use dictinary
class Solution2:
    def solve(self,s1,s2):
        dict1=defaultdict(int)
        m=len(s1)
        dict2=defaultdict(int)
        for i in s1:
            dict1[i]+=1
        for i,value in enumerate(s2):
            if i>=m:
                if dict1==dict2:
                    return True
                dict2[s2[i-m]]-=1
                if dict2[s2[i-m]]==0:
                    dict2.pop(s2[i-m])
            dict2[value]+=1
        if dict1==dict2:return True
            
        return False
solve2=Solution2()
print(solve2.solve("adc","dcda"))