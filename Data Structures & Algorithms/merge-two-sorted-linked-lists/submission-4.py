# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        cur = out
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            
            cur = cur.next
        if node1:
            cur.next = node1
        elif node2:
            cur.next = node2
        return out.next