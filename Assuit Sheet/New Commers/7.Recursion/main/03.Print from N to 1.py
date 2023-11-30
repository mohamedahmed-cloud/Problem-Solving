def PrintNumber(n,ans):
    if n==0:
        return ans
    ans.append(n)
    return PrintNumber(n-1,ans)



import sys
n=int(sys.stdin.readline())
ans=[]
print(*PrintNumber(n,ans))