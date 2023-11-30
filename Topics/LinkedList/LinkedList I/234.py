# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        store = []

        while head:
            store.append(head.val)
            head = head.next

        if store == store[::-1]:
            return True
            
        return False