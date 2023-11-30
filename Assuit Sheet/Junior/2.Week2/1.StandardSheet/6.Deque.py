import sys
from collections import deque
d=deque("")
n=int(sys.stdin.readline())
for i in range(n):
    take=sys.stdin.readline().split()
    if take[0]=="push_back":
        d.append(take[1])
    elif take[0]=="push_front":
        d.appendleft(take[1])
    elif take[0]=="pop_front":
        d.popleft()
    elif take[0]=="pop_back":
        d.pop()
    elif take[0]=="front":
        print(d[0])
    elif take[0]=="back":
        print(d[-1])
    elif take[0]=="print":
        print(d[int(take[1])-1])