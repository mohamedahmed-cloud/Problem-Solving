# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
           return None
        
        store = head

        while head:
            if head.next:
                if head.val == head.next.val:
                    head.next =  head.next.next
                else:
                    head = head.next
            else:
                head = head.next
            
        return store

         

            


