from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dict = {None:None}
        curr = head

        while curr :
            dict[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        
        while curr:
            dict[curr].next = dict[curr.next]
            dict[curr].random = dict[curr.random]
            curr = curr.next

        return dict[head]


