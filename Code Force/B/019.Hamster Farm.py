#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,k =map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
selected=0
num=0
previous=10e40
for i,value in enumerate(l):
    x=n%value
    if x<previous:
        selected=i+1
        num=n//value
    previous=min(previous,x)
print(selected,num)