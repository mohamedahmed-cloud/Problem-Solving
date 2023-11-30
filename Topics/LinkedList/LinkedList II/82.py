# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        x = curr = ListNode(102)
        curr.next = head
        last = 0
        while curr:
            if curr.next and curr.next.val == curr.val:
                temp = curr

                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                curr = last
                curr.next = temp.next
            else:
                last = curr
                curr = curr.next

        return x.next

