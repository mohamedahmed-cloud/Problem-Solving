#    Author : Mohamed Yousef 
#    Date   : 2023-01-05
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(points):
    points.sort()
    n=len(points)
    i=0
    ans=n
    while i<n-1:
        x=points[i]
        z=x[1]
        if z>=points[i+1][0]:
            ans-=1
            points[i+1]=[max(points[i][0],points[i+1][0]),min(points[i][1],points[i+1][1])]
        i+=1
        
    return ans

print(solve([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))