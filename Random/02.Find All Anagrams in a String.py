#    Author : Mohamed Yousef 
#    Date   : 2023-02-05
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()

class Solution:
    def solve(self,s,p):
        x=len(p)-1
        mySet=set()
        dict1=defaultdict(int)
        dict2=defaultdict(int)
        for i in p:
            dict1[i]+=1
        i=0
        for i,value in enumerate(s):
            dict2[value]+=1
            if x<=i:
                # print(dict1,dict2,dict1==dict2)
                if dict1==dict2:
                    mySet.add(i-x)
                dict2[s[i-x]]-=1
                if dict2[s[i-x]]==0:
                    dict2.pop(s[i-x])
        if dict1==dict2:
            mySet.add(i-x)
        return mySet
solve=Solution()
print(solve.solve("cbaebabacd","abc"))

# by Freq areray
class Solution:
    def solve(self,s,p):
        l1=[0]*26
        l2=[0]*26
        m=len(p)-1
        ans=set()
        for i in p:
            l1[ord(i)-ord("a")]+=1
        i=0
        for i,value in enumerate(s):
            l2[ord(value)-ord("a")]+=1
            if i>=m:
                if l1==l2:
                    ans.add(i-m)
                l2[ord(s[i-m])-ord("a")]-=1
        if l1==l2:
            ans.add(i-m)
        return ans



solve=Solution()
print(solve.solve( "cbaebabacd","abc"))