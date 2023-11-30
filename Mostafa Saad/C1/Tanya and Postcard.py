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

main = svalues()
sec = svalues()
finalyaya = 0
finalwhoops = 0

def create(main, sec):
    arr1Upper = [0] * 26
    arr1Lower = [0] * 26
    arr2Upper = [0] * 26
    arr2Lower = [0] * 26
    for i in main:
        if ord(i) >= 65 and ord(i) <= 91 :
            arr1Upper[ord(i) - ord("A")] += 1
        else:
            arr1Lower[ord(i) - ord("a")] += 1
    for i in sec:
        if ord(i) >= 65 and ord(i) <= 91 :
            arr2Upper[ord(i) - ord("A")] += 1
        else:
            arr2Lower[ord(i) - ord("a")] += 1
    
    return (arr1Upper, arr1Lower, arr2Upper, arr2Lower)


# to check lower1 & lower2 in each one.
def check(arr1,arr2,yaya = 0):
    for i in range(26):
        if arr1[i] >= arr2[i]:
            arr1[i] -= arr2[i]
            yaya += arr2[i]
            arr2[i] = 0
        else:
            arr2[i]  -= arr1[i]
            yaya += arr1[i]
            arr1[i] = 0
    return (yaya, arr1, arr2)
# to add upper & lower after call check.
def add(arr1,arr2):
    for i in range(26):
        arr1[i] += arr2[i]
    return arr1[i]

arr1Upper, arr1Lower, arr2Upper, arr2Lower=create(main, sec)
yaya,arr1Upper, arr2Upper = check(arr1Upper, arr2Upper)
finalyaya += yaya
yaya,arr1Lower, arr2Lower = check(arr1Lower, arr2Lower)
finalyaya += yaya
arrlLower = add(arr1Lower, arr1Upper)
arr2Upper = add(arr2Lower, arr2Upper)
whoops, arr1Lower, arr1Upper = check(arr1Lower, arr2Lower)
finalwhoops = whoops
print(finalyaya, finalwhoops)
