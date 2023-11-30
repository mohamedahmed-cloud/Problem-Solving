#    Author : Mohamed Yousef 
#    Date   : 2023-01-08
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
# First hard problem I manage solve in leet code 2023-01-08 😊😍
def solve(points):
    myDict=defaultdict(int)
    # find the solve 
    points.sort()
    n=len(points)
    for i in range(n):
        for j in range(i+1,n):
            x0=points[i][0]
            y0=points[i][1]
            x1=points[j][0]
            y1=points[j][1]
            try:
                slope=(y1-y0)/(x1-x0)
                # add str(i) to change slope if equal previous slope in next outer for loop.
                slope=str(slope)+str(i)
            except:
                # add str(i) to change slope if equal x0 in next outer for loop.
                slope="x0"+str(i)
            if myDict[slope]==0:
                myDict[slope]+=2
            else:
                myDict[slope]+=1
    print(myDict)
    try:
        return max(myDict.values())
    except:return 1

print(solve([[4,5],[4,-1],[4,0]]))

# A Greate problem I'm Very happy to manage to solve it.