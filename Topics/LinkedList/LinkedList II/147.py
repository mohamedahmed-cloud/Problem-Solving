#!/usr/bin/python3
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    
        if not head or not head.next:return head

        curr = head
        dummy = ListNode()

        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            x = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = x


        return dummy.next



