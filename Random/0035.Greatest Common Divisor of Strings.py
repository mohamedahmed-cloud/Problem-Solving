#    Author : Mohamed Yousef 
#    Date   : 2023-02-01
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,str1,str2):
        if str1+str2!=str2+str1:
            return ""
        x=len(str1)
        y=len(str2)
        a=math.gcd(x,y)
        s11=str1[:a]
        s12=str2[:a]
        s21=str1[-a:]
        s22=str2[-a:]
        def long(s1,s2):
            t1=""
            x=min(len(s1),len(s2))
            for i in range(x):
                if s1[i]==s2[i]:
                    t1+=s1[i]
                else:
                    return t1
            return t1
        s1=long(s11,s12)
        print(s21,s22)
        s2=long(s21[::-1],s22[::-1])[::-1]
        print(s1,s2)
        res=long(s1,s2)
        return res


solve=Solution()
print(solve.solve("ABABBD","ABBD"))

def solve(str1,str2):
    if str1+str2==str2+str1:
        return str1[:math.gcd(len(str1,str2))]
    return ""