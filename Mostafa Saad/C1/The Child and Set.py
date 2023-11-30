#    Author : Mohamed Yousef 
#    Date   : 2023-04-30
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

sum, limit = mvalues()
def TwoDArray (sum,limit):
    arr = []
    for i in range(limit,0,-1):
        count = 0
        constant = i
        while constant % 2 != 1:
            constant = constant // 2
            count += 1
        temp = [i, 2 ** count]
        arr.append(temp)
    return arr
def solve(sum,limit):
    arr=TwoDArray(sum,limit)
    ans = []
    i = 0
    while sum != 0 and i < limit:
        if sum - arr[i][1]  >= 0:
            sum -= arr[i][1]
            ans.append(arr[i][0])
        i += 1
    if sum == 0:
        return (len(ans), ans)
    return (-1,-1)
n, ans =solve(sum, limit)
if n != -1:
    print(n)
    sys.stdout.write(" ".join(map(str,ans)) + "\n")
else:
    print(-1)



