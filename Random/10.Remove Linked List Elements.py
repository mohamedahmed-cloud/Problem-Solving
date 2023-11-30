# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(next = head)
        curr=head
        dummy=prev
        while curr:
            if curr.val==val:
                dummy.next=curr.next
            else:
                dummy=curr
            curr=curr.next
        return prev.next
