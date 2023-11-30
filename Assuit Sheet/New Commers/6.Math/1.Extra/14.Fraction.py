import sys,math
n=int(sys.stdin.readline())
if n%2==0:
    f=n//2
    a=f-1
    b=f+1
    while True:
        if math.gcd(a,b)==1:
            print(a,b)
            break
        else:
            a-=1
            b+=1
else:
    f=n//2
    a=f
    b=f+1
    while True:
        if math.gcd(a,b)==1:
            print(a,b)
            break
        else:
            a-=1
            b+=1



