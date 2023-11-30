import sys,math
stack =[]
n=int(sys.stdin.readline())
for i in range(n):
    take=sys.stdin.readline().split()
    if take[0]=='push':
        stack.append(int(take[1]))
    elif take[0]=='pop':
        stack.pop()
    else:
        print(stack[-1])