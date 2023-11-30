# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional,List
from collections import deque

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        arr = deque()
        while head:
            arr.append(head.val)
            head = head.next

        x = [0] * (int(1e4) + 2)
        print(len(x))
        for i in nums:
            x[i] = 1
        cnt = 0
        ans = 0
        for i in arr:
            if x[i] == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 1:
                ans += 1

        return ans
