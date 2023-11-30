# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.getSize(head)
        minLen = n // k
        more = n % k
        parts = []
        curr = ListNode(0)
        curr.next = head

        for i in range(k):
            temp = curr
            for j in range(minLen + int(i < more)):
                curr = curr.next
            parts.append(temp.next)
            temp.next = None

        return parts


    def getSize(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n