# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        store = new = ListNode(next = head)

        while new:
            if new.next:
                if new.next.val == val:
                    new.next  = new.next.next
                else:
                    new = new.next
            else:
                if new.val == val:
                    new.next = None
                else:
                    new = new.next
        
        return store.next
