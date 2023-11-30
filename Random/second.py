#    Author : Mohamed Yousef 
#    Date   : 2023-02-07
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
try:
    f=open("read.txt","r")
    # f.readline()
except:
    print("file not found")
    quit()
store=dict()
for i in file:
    x=["id","name","grade","birthyear","gender"]
    iter=0
    for j in i:
        store[x[i]]=i[iter]
# print(store)
print("#"*30)




