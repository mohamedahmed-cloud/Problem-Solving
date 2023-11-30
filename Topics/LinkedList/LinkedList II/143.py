# Definition for singly-linked list.
from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = deque()
        curr = head

        while curr:
            l.append(curr.val)
            curr = curr.next

        curr = head.next
        ans = res = ListNode(l[0])
        flag = True
        iter = 1
        
        while curr:
            if flag:
                flag = False
                res.next = ListNode(l[-iter])
            else:
                flag = True
                res.next = ListNode(l[iter])
                iter += 1
            res = res.next
            curr = curr.next

        head.next = ans.next
        
       

# Second Solution.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        # truncate the array.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        side2 = slow.next
        slow.next = None

        # reverse second side
        curr = side2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        list1,list2 = head, prev
        
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2




       

        