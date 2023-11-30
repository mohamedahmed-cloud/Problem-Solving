from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = curr = ListNode(0)
        
        while left and right:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        dummy.next = left or right
        
        return curr.next
    
def makeLinkedList(head):
    curr = save = ListNode(0)
    for i in head:
        curr.next = ListNode(i)
        curr = curr.next
    return save.next


solve = Solution()
x = makeLinkedList([4,2,1,3])
slv = solve.sortList(x)
while slv:
    print(slv.val)
    slv = slv.next
