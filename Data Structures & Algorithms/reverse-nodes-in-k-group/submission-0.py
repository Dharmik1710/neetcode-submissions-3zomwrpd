# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        while k > 0:
            next = head.next
            head.next = prev
            prev = head
            head = next
            k-=1
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        curr = head
        rev = res
        while curr:
            begin = curr
            i = 0
            while i < k:
                if not curr:
                    return res.next
                curr = curr.next
                i+=1
            
            rev.next = self.reverse(begin, k)
            rev = begin
            begin.next = curr
        return res.next