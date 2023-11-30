# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        save = []
        s1 = s2 =list1
       
        cnt = 1
        while list1 and cnt < a:
            list1 = list1.next
            cnt += 1
        while s2:
            save.append(s2.val)
            s2 = s2.next

        while list2:
            list1.next = list2
            list1 = list1.next
            list2 = list2.next
        skip = b + 1
        save = save[skip : ]
        for i in save:
            list1.next = ListNode(val = i)
            list1 = list1.next

        print(save)
        return s1

