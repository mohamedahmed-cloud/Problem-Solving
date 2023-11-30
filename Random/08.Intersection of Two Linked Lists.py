#    Author : Mohamed Yousef 
#    Date   : 2023-02-09
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(headA):
            ans=0
            while headA:
                ans+=1
                headA=headA.next
            return ans
        lenA=length(headA)
        lenB=length(headB)
        compareA=headA
        compareB=headB
        while lenA>lenB:
            lenA-=1
            compareA=compareA.next
        while lenA<lenB:
            lenB-=1
            compareB=compareB.next
        while compareA!=compareB:
            compareA=compareA.next
            compareB=compareB.next
        return compareA
