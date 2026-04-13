# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        while head:
            prevNode = out.next
            out.next = ListNode(head.val, prevNode)
            head = head.next
        return out.next