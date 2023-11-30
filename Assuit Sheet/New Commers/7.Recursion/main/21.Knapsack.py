def knapsack(n,capacity,weights,value):
    if n==0 or capacity==0:
        return 0    
    if weights[n-1]>capacity:
        return knapsack(n-1,capacity,weights,value)
    else:
        return max((value[n-1]+knapsack(n-1,capacity-weight[n-1],weights,value)),knapsack(n-1,capacity,weights,value))

import sys
n,c=map(int, sys.stdin.readline().split())
value,weight=[],[]
for i in range(n):
    x,y= map(int, sys.stdin.readline().split())
    weight.append(x)
    value.append(y)
print(knapsack(n,c,weight,value))