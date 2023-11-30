# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        prev_group = start_group = end_group = next_group = None
        prev_group = dummy = ListNode(0)
        ans = ListNode(0)
        cnt = 0
        while head:
            i, start_group = 1, head
            
            while k > i and head.next:
                head = head.next
                i += 1
                
            if k != i:break

            end_group = head
            next_group = head = head.next
            curr = start_group
            prev = None

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev_group.next = end_group
            prev_group = start_group
            start_group.next = next_group
            # if cnt == 1:
            #     return dummy
            # cnt += 1
        return dummy.next
