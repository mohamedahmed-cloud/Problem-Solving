#    Author : Mohamed Yousef 
#    Date   : 2022-12-20
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
# Will Buy if Next me Bigger than me
# Will Sell if After Lower than me
def solve(prices):
    n=len(prices)
    buy=-1
    profit=0
    for i in range(1,n):
        # Buy or not
        if prices[i-1]<prices[i] and buy==-1:
            buy=prices[i-1]
        if prices[i-1]>prices[i] and buy>=0:
            # Sell
            profit+=prices[i-1]-buy
            # print(profit)
            buy=-1
    # print(prices[-1],buy)
    if buy>=0 and prices[-1]>buy:
        profit+=prices[-1]-buy
    return profit

print(solve([2,1,2,0,1]))
