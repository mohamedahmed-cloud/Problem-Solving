import sys,math,bisect,itertools,collections
t=int(sys.stdin.readline())
l=set()
d={}
for _ in range(t):
    s=sys.stdin.readline().strip()
    try:
        d[s]+=1
        print(s+str(d[s]-1))
    except :
        d[s]=1
        print("OK")
    # print(d)