
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        num = 0
        
        while curr:
            num += 1
            curr = curr.next
        
        node = num - n
        if node == 0:
            return head.next

        curr = head
        num = 0

        while curr:
            num += 1
            if num == node:
                temp = curr
                temp = temp.next.next
                curr.next = temp
            else:
                curr = curr.next

            
        return head