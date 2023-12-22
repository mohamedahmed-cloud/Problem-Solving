#    Author : Mohamed Yousef 
#    Date   : 2023-12-22
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(str,sys.stdin.readline().split())
def lvalues():return list(map(str,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Values:
    def __init__(self,all):
        self.pos = int(all[1])
        self.statement = all[0]

arr = []
n = test()
for _ in range(n):
    arr.append(Values(lvalues()))
arr = sorted(arr, key=lambda x: x.pos)

# print(list(arr)[0].pos, arr[1].pos)
left_arr = [0] * (n)
right_arr = [0] * n

for i in range(1,  n):
    left_arr[i] += left_arr[i - 1]
    if arr[i - 1].statement == "L" and arr[i].pos != arr[i - 1].pos:
        left_arr[i] += 1

for i in range(n - 2, - 1, -1):
    right_arr[i] += right_arr[i + 1]
    if arr[i + 1].statement == "G" and arr[i].pos != arr[i + 1].pos:
        right_arr[i] += 1

ans = float("inf")
# print(list(left_arr), list(right_arr))
for i in range(n):
    ans = min(ans, left_arr[i] + right_arr[i], ans)
print(ans)