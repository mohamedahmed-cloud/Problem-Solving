# Memory Exceed
def palindrome(arr):
    n=len(arr)
    if n==0 or n==1:
        return True
    if arr[0]==arr[n-1]:
        return palindrome(arr[1:n-1])
    return False
import sys,math
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
# print(arr)
# a=palindrome(arr)

# Accepted with iteration
for i in range(n):
    if arr[i]==arr[n-i-1]:
        pass
    else:
        print("NO")
        quit()
print("YES")


