from re import A
import sys
sn,sl=map(int,sys.stdin.readline().split())
string=input()
# string=string[:-1]
for i in range(sl):
    take=input().split()
    # print(take)
    # easy
    if take[0]=="pop_back":
        string=string[:-1]
    elif take[0]=="front":
        print(string[0])
    elif take[0]=="back":
        print(string[-1])
    elif take[0]=="substr":
        a=int(take[1])
        b=int(take[2])
        l=min(a,b)
        r=max(a,b)
        print(string[l-1:r])
    elif take[0]=="print":
        print(string[int(take[1])-1])
    elif take[0]=="push_back":
        string=string+take[1]    
        # hard
    elif take[0]=="reverse":
        a=int(take[1])
        b=int(take[2])
        l=min(a,b)
        r=max(a,b)
        # print(string)
        string=string[:l-1]+"".join(reversed(string[l-1:r]))+string[r:]
        # print(string)
        # print(string)
    elif take[0]=="sort":
        a=int(take[1])
        b=int(take[2])
        l=min(a,b)
        r=max(a,b)
        # print(string)
        string=string[:l-1]+"".join(sorted(string[l-1:r]))+string[r:]
        # print(string)