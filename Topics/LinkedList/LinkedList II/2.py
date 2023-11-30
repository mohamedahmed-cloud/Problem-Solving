# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    
        add = n = n1 = n2 = 0
        toLoop1 = l1
        toLoop2 = l2

        while toLoop1:
            n1 += 1
            toLoop1 = toLoop1.next

        while toLoop2:
            n2 += 1
            toLoop2 = toLoop2.next

        if n1 < n2:
            l1, l2 = l2, l1
        
        s1   = l1

        prev = 0
        
        while l1 and l2:
            l1.val = (l1.val + l2.val + add)
            add = l1.val // 10
            l1.val = l1.val % 10
            n += 1
            prev = l1
            l1 = l1.next
            l2 = l2.next

        if l1 and add != 0:
            while l1 and add != 0:
                l1.val = (l1.val  + add)
                add = l1.val // 10
                l1.val = l1.val % 10
                prev = l1
                l1 = l1.next

        if add != 0 and prev:
            prev.next = ListNode(add)

        return s1
