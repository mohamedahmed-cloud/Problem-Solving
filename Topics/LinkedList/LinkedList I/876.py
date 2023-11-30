# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        dummyNode = head
        while (dummyNode):
            array.append(dummyNode.val)
            dummyNode = dummyNode.next
        for i in range(len(array) // 2):
            head = head.next
        return head