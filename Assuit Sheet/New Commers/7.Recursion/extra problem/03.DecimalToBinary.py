def DecimalToBinary(n,ans):
    
    if  n==0:
        return ans[::-1]
    ans+=str(n%2)
    return DecimalToBinary(n//2,ans)
    



import sys
n=int(sys.stdin.readline())
ans=""
print(DecimalToBinary(n,ans))