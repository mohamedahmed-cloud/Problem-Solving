#    Author : Mohamed Yousef 
#    Date   : 2023-02-14
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,a,b):
        n=len(a)
        m=len(b)
        if m>n:
            a,b=b,a
            n,m=m,n
        ans=""
        reminder=""
        a=a[::-1]
        b=b[::-1]
        for i in range(m):
            x=a[i]
            y=b[i]
            if x=="1" and y=="1":
                if reminder=="1":
                    ans+="1"
                else:
                    ans+="0"
                    reminder+="1"
                    reminder=reminder[::-1]
            elif x=="1":
                if reminder=="1":
                    ans+="0"
                else:
                    ans+="1"
            elif y=="1":
                if reminder=="1":
                    ans+="0"
                else:
                    ans+="1"
            else:
                if reminder=="1":
                    ans+=reminder[0]
                    reminder=reminder[1:]
                else:
                    ans+="0"
            if len(reminder)>=2:
                print(reminder,i,x,y)
                break
        for i in range(m,n):
            if reminder=="1":
                if a[i]=="1":
                    ans+="0"
                else:
                    ans+="1"
                    reminder=reminder[1:]
            else:
                ans+=a[i]
        ans+=reminder
        # if "0":print("ljd")
        return ans[::-1]
solve=Solution()
print(solve.solve("1011","1010"))
# Easy Way to solve

class Solution:
    def solve(self,a,b):
        a=int(a,2)
        b=int(b,2)
        return bin(a+b)[2:]



solve=Solution()
print(solve.solve("1011","1010"))
