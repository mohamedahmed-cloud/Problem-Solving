#    Author : Mohamed Yousef 
#    Date   : 2022-12-16
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
short={}
long={}
def decode(longUrl):
    l=longUrl.split("/")
    count=0
    x=""
    for i in l:
        if i=="":
            i="/"
        x+=str(count)
        short[i]=str(count)
        long[str(count)]=i
        count+=1
    return encode(x)
def encode(token):
    ans=""
    print(long)
    for i in token:
        ans+=long[i]
        if long[i] !="/":
            ans+="/"
    return ans[:-1]
print(decode("https://leetcode.com/problems/design-tinyurl"))
