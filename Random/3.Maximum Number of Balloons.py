#    Author : Mohamed Yousef 
#    Date   : 2022-12-10
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(str):
    freq=[0]*26
    for i in str:
        freq[ord(i)-97]+=1
    # print(freq)
    b=freq[ord("b")-97]
    a=freq[ord("a")-97]
    l=freq[ord("l")-97]//2
    o=freq[ord("o")-97]//2
    n=freq[ord("n")-97]
    return min(a,b,l,o,n)
print(solve("leetcode"))
def solve2(str):
    dic=defaultdict(int)
    for i in "balon":
        dic[i]=0
    for i in str:
        if i in "balon":
            dic[i]+=1
    for s,n in dic.items():
        if s in "lo":
            dic[s]=n//2
    return min(dic.values())
print(solve2("llobo"))

