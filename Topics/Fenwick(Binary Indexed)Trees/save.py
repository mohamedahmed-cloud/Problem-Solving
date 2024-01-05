#    Author : Mohamed Yousef 
#    Date   : 2024-01-01
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(str,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


MAXN = 10**6 + 5
MAXV = 5 * 10**5
MOD = 10**9 + 7

N, Q = 0, 0
a = [0] * MAXN
phi = [0] * (MAXV + 5)
p = [0] * (MAXV + 5)
BIT = [0] * MAXN

def mod(x):
   return (x % MOD + MOD) % MOD

def compute_phi():
   for i in range(1, MAXV + 1):
       phi[i] = i
   for i in range(2, MAXV + 1):
       if phi[i] == i:  # prime number
           for j in range(i, MAXV + 1, i):
               phi[j] -= phi[j] // i
               phi[j] = mod(phi[j])

def compute_pillai():
   for i in range(1, MAXV + 1):
       for j in range(i, MAXV + 1, i):
           p[j] += i * phi[j // i]
           p[j] = mod(p[j])

def update(i, val):
   while i <= N:
       BIT[i] += val
       BIT[i] = mod(BIT[i])
       i += i & -i

def query(i):
   sum = 0
   while i > 0:
       sum += BIT[i]
       sum = mod(sum)
       i -= i & -i
   return sum

compute_phi()
compute_pillai()

# Input and queries
N = int(input())
l = lvalues()
for i in range(1, N + 1):
   a[i] = l[i - 1]
   update(i, p[a[i]])

Q = int(input())
for _ in range(Q):
   c, x, y = mvalues()
   x, y = int(x), int(y)
   if c == 'U':
       update(x, mod(-p[a[x]] + p[y]))
       a[x] = y
   elif c == 'C':
       print(mod(query(y) - query(x) + p[a[x]]))
