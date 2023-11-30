from collections import Counter
def stringAnagram(dictionary, query):
    dp = ["".join(sorted(s)) for s in dictionary]
    q = ["".join(sorted(s)) for s in query]
    ans = []
    a = Counter(dp)
    for s in q:
        if s not in a.keys():
            ans.append(0)
        else:
            ans.append(a[s])
    return ans

# def stringAnagram(dictionary, query):
#     for i in dictionary:
#         for j i

# import sys
# dictionary=list(map(str,sys.stdin.readline().split()))
# query=list(map(str,sys.stdin.readline().split()))