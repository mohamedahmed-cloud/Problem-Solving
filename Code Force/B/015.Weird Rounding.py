#    Author : Mohamed Yousef 
#    Date   : 2022-12-04
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,k =map(int,sys.stdin.readline().split())
n=str(n)
# print(n)
zero=0
removed=0
for i in n[::-1]:
    # print(i)
    if zero==k:
        print(removed)
        quit()
    if i=="0":
        zero+=1
    else:
        removed+=1

print(len(n)-1)


