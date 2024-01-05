#    Author : Mohamed Yousef 
#    Date   : 2023-12-24
import sys
from collections import defaultdict

sys.setrecursionlimit(50000)

def svalues():
    return sys.stdin.readline().strip()

def test():
    return int(sys.stdin.readline())

def dfs(s, i, ans):
    if ans[s] == 1:
        return
    ans[s] = 1
    if not s[1:]:   
        ans[s] = 1
        return
    dfs(s[1:], 0, ans) 
    dfs(s[0] + s[2:], 1, ans)


for _ in range(test()):
    n = test()
    s = svalues()
    ans = defaultdict(int)

    dfs(s, 0, ans)
    print(len(ans))
