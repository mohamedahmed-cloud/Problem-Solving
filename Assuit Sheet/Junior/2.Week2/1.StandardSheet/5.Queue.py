import sys,math
queue=[]
n=int(sys.stdin.readline())
for i in range(n):
    take=sys.stdin.readline().split()
    if take[0]=="push":
        queue.append(take[1])
    elif take[0]=="pop":
        queue.pop(0)
    elif take[0]=="back":
        print(queue[-1])
    elif take[0]=="front":
        print(queue[0])
    