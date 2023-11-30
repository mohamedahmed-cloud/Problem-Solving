#    Author : Mohamed Yousef 
#    Date   : 2023-02-01
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

def solve(n,arr):
    Min=min(arr)
    Max=max(arr)
    freq=[0]*int(1e5+1)
    for i in arr:
        freq[i]+=1
    i=1
    check=0
    x=Max+1-Min
    # print(freq[Min:Max+1])
    while i!=0:
        check=0
        for i in range(Min,Max+1):
            if freq[i]>0:print(i,end=' ')
            freq[i]-=1
            if freq[i]<=0:
                check+=1
            if check==x:
                i=0
                break
        print()



if __name__ == '__main__':
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    solve(n,arr)