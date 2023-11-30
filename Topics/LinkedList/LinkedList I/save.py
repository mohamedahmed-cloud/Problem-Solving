# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        dummy1 = list1
        dummy2  = list2
        result = []
        head = ListNode(0)

        while list1:
            arr1.append(list1.val)
            list1 = list1.next
        
        while list2:
            arr2.append(list2.val)
            list2 = list2.next
        i, j = 0 , 0 
        def isValid(i, j):
            # print(i,j)
            return i < len(arr1) and j < len(arr2)

        while isValid(i, j):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1

        for _ in range(i,len(arr1)):
            result.append(arr1[_])

        for _ in range(j, len(arr2)):
            result.append(arr2[_])

        # print(result)
        for i in range(len(result)):
            head.val = result[i]
            head = head.next 
        return head



