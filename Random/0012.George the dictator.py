#    Author : Mohamed Yousef 
#    Date   : 2023-02-01
# Give me Wrong Answer in Test case 4
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

def solve(n,k,arr):
        ans=0
        hashTable=defaultdict(int)
        for _ in arr:
            hashTable[_]+=1
        if n==1:return 0
        for x,y in hashTable.items():
            needed1=hashTable.get(k-x,"fms")
            needed2=hashTable.get(x-k,"fms")
            i=j=0
            if needed1!="fms":
                i=max(needed1,0)
            if needed2!="fms":
                j=max(needed2,0)
            pre=min(y,i+j)
            if pre>1:ans+=pre*2
            else:ans+=pre
            if y>0:
                if y>i:
                    y-=i
                    i=0
                else:
                    i-=y
                    y=0
            if y>0:
                if y>j:
                    y-=j
                    j=0
                else:
                    i-=y
                    y=0
            if needed1!="fms":hashTable[k-x]=i
            if needed2!="fms":hashTable[x-k]=j
            hashTable[x]=y
        return ans
if __name__=="__main__":
    n,k=map(int,sys.stdin.readline().split())
    l=list(map(int,sys.stdin.readline().split()))
    print(solve(n,k,l))
