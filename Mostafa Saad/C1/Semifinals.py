#    Author : Mohamed Yousef 
#    Date   : 2023-05-04
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

t = test()
arr1 = []
arr2 = []
all = []
for _ in range(t):
    a,b=mvalues()
    arr1.append(a)
    arr2.append(b)
p1 = 0
p2 = 0
for _ in range(2*t):
    if p1 < t and p2 < t :
        if arr1[p1] > arr2[p2]:
            all.append(arr2[p2])
            p2 += 1
        else:
            all.append(arr1[p1])
            p1 += 1
if p1 < t:
    all.extend(arr1[p1:])
if p2 < t:
    all.extend(arr2[p2:])

# print(all)
# print(arr1)
# print(arr2)

now = all[:t]
# arr3 = set(arr1)
# arr4 = set(arr2)

s1 = ""
s2 = ""
n1 = 0
n2 = 0
for i in now:
    f1 = bisect.bisect_left(arr1,i)
    f2 = bisect.bisect_left(arr2,i)
    # print(f1, f2)
    if f1 != t and arr1[f1] == i:
        s1 += "1"
        n1 += 1
    if f2 != t and arr2[f2] == i:
        s2 += "1"
        n2 += 1
n11 = n1
n22 = n2
# print(s1,s2)
for i in range(t//2):
    if i >= n1:
        s1 += "1"
        n11 += 1
    if i >= n2:
        s2 += "1"
        n22 += 1

if n11 < t:
    s1 += "0" * (t - n11)
if n22 < t:
    s2 += "0" * (t - n22)

print(s1)
print(s2)