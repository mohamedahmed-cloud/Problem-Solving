
#    Author : Mohamed Yousef 
#    Date   : 2022-12-07
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque

arr=[(1,2),(3,4)]
for i in range(len(arr)):
    a=bisect.bisect_left(arr,(1,3))
    print(a)
