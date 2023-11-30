# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
from collections import deque

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x = deque()
        dummy = d1 = head

        while dummy:
            x.append(dummy.val)
            dummy = dummy.next
        
        y1 = x[k - 1]
        y2 = x[-k]
        l = len(x)
        change1 = k
        change2 = l - k + 1
        i = 1
        # print(x,y1,y2)
        while d1:
            if i == change1:
                d1.val = y2
            elif i == change2:
                d1.val = y1

            d1 = d1.next
            i += 1
        return head

