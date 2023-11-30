#    Author : Mohamed Yousef
#    Date   : 2022-12-21
import sys
import math
import bisect
import collections
import itertools
import heapq
from collections import defaultdict, deque
sys.setrecursionlimit(50000)  # To increase Recursion depth in py

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
ans = "WRONGANSWER"
if len(s) >= k:
    if n==k:
        ans=s
    if n < k:
        # print("flkj")
        pass
    else:
        if k == 0:
            freq = [0]*26
            for i in s:
                freq[ord(i)-ord("a")] += 1
            for i in range(26):
                if freq[i] == 0:
                    ans = chr(i+ord("a"))*n
                    break
        else:
            freq = [0]*26
            for i in s[k:]:
                freq[ord(i)-ord("a")] += 1
            find = ""
            for i in range(26):
                if freq[i] == 0:
                    find = chr(i+ord("a"))
                    break
            if find:
                ans = s[:k]+find*(n-k)
            else:
                ans=s[:k]
                ans+="A"*(n-k)

print(ans)
