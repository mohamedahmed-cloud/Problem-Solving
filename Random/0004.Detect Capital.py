#    Author : Mohamed Yousef 
#    Date   : 2023-01-02
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(word):
    num=0
    n=0
    for i in word:
        n+=1
        if i.upper() ==i:
            num+=1
        else:
            if num>1:
                return False
    # print(num,n)
    if n==num or num==0 or word[0].upper()==word[0] and num==1:
        return True
    return False

# another solution
def solve2(word):
    return (word==word.capitalize() or
            word==word.upper() or 
            word==word.lower())
print(solve2("aFLG"))
def solve3(word):
    return word.isupper() or word.isTitle() or word.islower()
print(solve2("aFLG"))