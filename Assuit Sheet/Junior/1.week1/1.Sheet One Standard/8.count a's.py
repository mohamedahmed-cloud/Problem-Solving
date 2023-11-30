import sys,math
s=sys.stdin.readline()
s=s[:-1]
n=int(sys.stdin.readline())
for i in range(n):
    st,e=map(int,sys.stdin.readline().split())
    # print(s[0:])
    # print(s[st-1:e])
    print(s[st-1:e].count("a"))


