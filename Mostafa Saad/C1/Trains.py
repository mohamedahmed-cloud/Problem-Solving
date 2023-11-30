#    Author : Mohamed Yousef 
#    Date   : 2023-05-03
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

a, b = mvalues()
Dasha = a 
Masha = b


c = math.lcm(a, b)
count = 1
big = a * b
# print(c)
while c * count < big:
    count += 1 
    # c *= count

if a < b:
    Dasha += count
else:
    Masha += count

# print(Dasha, Masha)

if Dasha == Masha:
    print("Equal")
elif Dasha < Masha:
    print("Dasha")
else:
    print("Masha")