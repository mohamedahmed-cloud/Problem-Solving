
# Definition for a Node.

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

from typing import Optional
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head

        while curr:
            if not curr.child:
                curr = curr.next
            else:
                temp = curr.child
                while temp.next:
                    temp = temp.next
                
                temp.next = curr.next

                while temp.next:
                    temp.next.prev = temp
                    temp = temp.next
                
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None

        return head