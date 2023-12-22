#    Author : Mohamed Yousef 
#    Date   : 2023-12-18
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

count = [0] * 32
for _ in range(test()):
    n, val = mvalues()
    if n == 1:
        count[val] += 1

    if n == 2:
        bin_value = bin(val)[2:][::-1]
        bin_length = len(bin_value)
        tmp = count[:]
        ans = "YES"
        # print(bin_value, tmp[:10])
        for i in range(bin_length):
            if bin_value[i] == "1":
                if tmp[i] >= 1:
                    tmp[i] -= 1
                else:
                    ans = "NO"
                    break
            tmp[i + 1] += tmp[i] // 2
        print(ans)
