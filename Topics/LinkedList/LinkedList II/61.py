# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
    
        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1
        
        k = k % n
        if k == 0:
            return head

        curr = head
        prev = 0
        rotate = None

        while curr:
            if n == k:
                rotate = curr 
                prev.next = None
                break
            n -= 1
            prev = curr
            curr = curr.next
        
        curr = rotate

        while curr:
            prev = curr 
            curr = curr.next

        prev.next = head

        return rotate 
        