# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummy = dummy2 = head
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next

        while head:
            head.val = arr[-1]
            arr.pop()
            head = head.next

        return dummy2