# #    Author : Mohamed Yousef 
# #    Date   : 2023-06-27
# import sys,math,bisect,collections,itertools,heapq
# from itertools  import accumulate ,combinations ,permutations,chain
# from collections import defaultdict,deque,Counter
# sys.setrecursionlimit(50000) #To increase Recursion depth in py
# def mvalues():return map(int,sys.stdin.readline().split())
# def lvalues():return list(map(int,sys.stdin.readline().split()))
# def svalues():return sys.stdin.readline().strip()
# def test():return int(sys.stdin.readline())



# Not Yet.

# for _ in range(test()):

#     n, m = mvalues()
#     m -= 1
#     l = lvalues()
#     ans = 0
#     if l[m] > 0 and n != 1:
#         ans += 1
#         l[m] = -l[m]

#     target = sum(l[: m + 1])
#     freq = [0] * n
#     freq[0] = l[0]

#     for i in range(1,n):

#         freq[i] = (freq[i -1] + l[i])
#         if freq[i] < target:
#             freq[i] = (freq[i - 1] - l[i])
#             if i <= m:
#                 target = freq[i] + sum(l[i + 1 : m+1])

#             ans += 1
#     # print(freq)
#     print(ans)


        


