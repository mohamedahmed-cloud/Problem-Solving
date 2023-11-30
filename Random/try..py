#    Author : Mohamed Yousef 
#    Date   : 2022-12-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
x=defaultdict(int)
for i in range(10):
    x[i]+=(i*10)
for i,k in x.items():
    print(i,k)