def Is_Palindrome(s):
    n=len(s)
    if n==0 or n==1:
        return True
    # print(s[0],s[n-1])
    if s[0]==s[n-1]:
        return Is_Palindrome(s[1:n-1])
    return False
import sys
s=sys.stdin.readline()
s=s[:-1]
print(Is_Palindrome(s))