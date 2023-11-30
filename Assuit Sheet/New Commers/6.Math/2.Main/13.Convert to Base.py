def toDecimal(n,x):
    return int(n,x)
def fromDeciaml(n,x):
    ans=""
    while n>0:
        ans+=str(convert(n%x))
        n=n//x
    ans=ans[::-1]
    return ans
def convert(num):
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))
import sys,math
t=int(input())
n,x=map(int,sys.stdin.readline().split())
if t==1:
    print(toDecimal(str(n),x))
if t==2:
    out=fromDeciaml(n,x)
    print(out)
