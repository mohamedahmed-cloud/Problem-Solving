#    Author : Mohamed Yousef 
#    Date   : 2022-12-29
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(numRows):
    x=[0]*2
    if numRows<=1:
        return [[1]]
    else:
        x[0]=[1]
        x[1]=[1,1]
        # print(x)
        # print(x[1])
        for i in range(2,numRows):
            add=[1]
            # print(x[i-1])
            for j in range(1,len(x[i-1])):
                add.append(x[i-1][j]+x[i-1][j-1])
            add.append(1)
            x.append(add)

            # print(add)
            # print(x)
    return x
print(solve(2))



