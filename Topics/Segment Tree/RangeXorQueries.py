#    Author : Mohamed Yousef 
#    Date   : 2023-12-05
import sys
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
n, m = mvalues()
l = lvalues()
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i -1] ^ l[i - 1]
# print(prefix)
for i in range(m):
    s, e = mvalues()
    print(prefix[s - 1] ^ prefix[e])
