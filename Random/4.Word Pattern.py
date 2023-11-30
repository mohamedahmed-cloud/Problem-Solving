#    Author : Mohamed Yousef 
#    Date   : 2022-12-10
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(pattern,s):
    our_dict=defaultdict()
    s=s.split(" ")
    x=0
    n=len(s)
    y=len(pattern)
    if n<y:return False
    if n%y!=0:return False
    our_set=set()
    for i in pattern:
        if s[x] in our_set:
            try:
                if our_dict[i]!=s[x]:
                    return False
            except:return False
        else:our_set.add(s[x])
        our_dict[i]=s[x]
        x+=1
    for i in range(n):
        if our_dict[pattern[i%x]]!=s[i]:
            return False
    return True
print(solve("aaa","aa"))
# Must to improve the performance of you algorithm
# another Solution Time complexity is O(n+m)
def solve2(pattern,s):
    s=s.split(" ")
    n=len(s)
    m=len(pattern)
    if n!=m:return False
    dict1=defaultdict()
    dict2=defaultdict()
    for i in range(n):
        if s[i] in dict1 and dict1[s[i]]!=pattern[i]:
            return False
        if pattern[i] in dict2 and dict2[pattern[i]]!=s[i]:
            return False
        dict1[s[i]]=pattern[i]
        dict2[pattern[i]]=s[i]
    return True
print(solve2("abba","dog"))
