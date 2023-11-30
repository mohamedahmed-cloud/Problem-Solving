#    Author : Mohamed Yousef 
#    Date   : 2022-12-07
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
a=int(sys.stdin.readline())
# a=536870911
add=1
while a!=1:
    if a%2==0:
        a//=2
    else:
        a-=1
        add+=1

print(add)