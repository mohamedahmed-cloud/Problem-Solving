import sys, math
from collections import defaultdict
 
sys.setrecursionlimit(10 ** 6)
 
 
def ain():  # takes array as input
    return list(map(int, sin().split()))
 
 
def sin():
    return input()
 
 
segTree = [0] * (2000000)
 
 
def make(l, r, ind):
    if l == r:
        segTree[ind] = 1
        return
    mid = (l + r) // 2
    make(l, mid, 2 * ind + 1)
    make(mid + 1, r, 2 * ind + 2)
    segTree[ind] = segTree[2 * ind + 1] + segTree[2 * ind + 2]
 
 
def qry(l, r, ind, val):
    ans = 0
    if l == r:
        segTree[ind] = 0
        ans = l
    elif val <= segTree[2 * ind + 1]:
        ans = qry(l, (l + r) // 2, 2 * ind + 1, val)
    else:
        ans = qry((l + r) // 2 + 1, r, 2 * ind + 2, val - segTree[2 * ind + 1])
    segTree[ind] = segTree[2 * ind + 1] + segTree[2 * ind + 2]
    return ans
 
 
def main():
    n = int(sin())
    arr = ain()
    qrys = ain()
    make(0, n - 1, 0)
    for i in qrys:
        ans = qry(0, n - 1, 0, i)
        print(segTree[:20])
        print(arr[ans], end=" ")
 


if __name__ == '__main__':
    main()
