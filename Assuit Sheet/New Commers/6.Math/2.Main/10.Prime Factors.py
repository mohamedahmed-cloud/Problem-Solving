def solve(n):
    arr=[]
    mod=2
    s=""
    while n>1:
        iter=0
        while n%mod==0:
            arr.append(mod)
            n=n//mod
            iter+=1
            
        else:
            if iter>0:
                s+=f"({str(mod)}^{str(iter)})*"
            iter=0
            mod+=1
    print(s[:-1])
    




import sys,math
n=int(sys.stdin.readline())
solve(n)