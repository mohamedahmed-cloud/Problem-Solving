# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        store1 = headA
        store2 = headB
        l1 = 0
        l2 = 0

        while headA:
            l1 += 1
            headA = headA.next

        while headB:
            l2 += 1
            headB = headB.next
        
        while l1 > l2:
            store1 = store1.next
            l1 -= 1

        while l2 > l1:
            store2 = store2.next
            l2 -= 1

        while store1 and store2:

            if store1 == store2:
                return store1
            
            store1 = store1.next
            store2 = store2.next

        return None
