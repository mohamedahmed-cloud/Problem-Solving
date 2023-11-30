# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if (not head or not head.next) or left == right :
            return head

        revs = None
        revend = None
        revs_prev = None
        revend_next = None
        curr = head
        def reverse(head):
            prev = None
            # store = head
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp

            return prev

        n = 1
        while curr:
            if n < left:
                revs_prev = curr

            elif n == left:
                revs = curr
            elif n == right:
                revend = curr
                revend_next = curr.next
            curr = curr.next
            n += 1
        
        revend.next = None
        revend = reverse(revs)

        if (revs_prev):
            revs_prev.next = revend
        else:
            head = revend

        revs.next = revend_next

        return head


