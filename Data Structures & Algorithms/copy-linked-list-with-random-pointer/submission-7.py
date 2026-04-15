"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            nn = Node(curr.val, curr.next, curr.random)
            curr.random = nn
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                curr.random.next = curr.next.random
            if curr.random.random:
                curr.random.random = curr.random.random.random
            curr = curr.next

        if head:
            return head.random
        return head