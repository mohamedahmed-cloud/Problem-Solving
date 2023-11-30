#    Author : Mohamed Yousef 
#    Date   : 2022-12-02
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,k=map(int,sys.stdin.readline().split())
s=sys.stdin.readline().strip()
freq=[0]*26
for i in s:
    freq[ord(i)-65]+=1
with_k=set()
# print(freq)
for i in s:
    freq[ord(i)-65]-=1
    if i not in with_k:
        k-=1
        with_k.add(i)
    if k<0:
        print("YES")
        quit()
    if freq[ord(i)-65]==0:
        k+=1
print("NO")
