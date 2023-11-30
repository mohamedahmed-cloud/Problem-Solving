import sys,math
def solve(a,b,w):
    x=min(a,b)-1
    y=max(a,b)
    x=x//w
    y//=w
    l=x*(x+1)/2
    h=y*(y+1)/2
    ans=h*w-l*w
    return int(ans)
   
    # return ans
a,b,w=map(int,sys.stdin.readline().split())
print(solve(a,b,w))