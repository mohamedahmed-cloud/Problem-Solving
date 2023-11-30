# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while head:
            arr.append(head.val)
            head = head.next
        s = 0
        for i in arr:
            if i < 0:
                s += i
            
        n = len(arr)
        for i in range(n):
            total = 0
            for j in range(i,n):

                if arr[j] != "fms":
                    total += arr[j]
                    if total == 0:
                        for x in range(i, j + 1):
                            arr[x] = "fms"
    
        head = curr = ListNode()

        for i in arr:
            if i != "fms":
                curr.next = ListNode(i)
                curr = curr.next
        return head.next


# This Solution beat more than 97% in TC
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = {}
        visited[0] = store = ListNode(0)
        ps = 0
        store.next = head

        while head:
            ps += head.val
            visited[ps] = head
            head = head.next
        
        head = store
        ps = 0
        
        while head:
            ps += head.val
            if visited[ps] != head :
                head.next = visited[ps].next
            
            head = head.next
        
        return store.next








        







        