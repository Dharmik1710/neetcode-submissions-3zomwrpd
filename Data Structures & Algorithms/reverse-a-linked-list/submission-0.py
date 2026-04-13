# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        node = head
        while node:
            prevNode = out.next
            out.next = ListNode(node.val, prevNode)
            node = node.next
        return out.next