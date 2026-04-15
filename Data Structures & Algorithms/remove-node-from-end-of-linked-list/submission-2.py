# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        while n > 0:
            second = second.next
            n -= 1
        
        while second and second.next:
            first, second = first.next, second.next
        
        if second:
            first.next = first.next.next
        else:
            head = first.next
        return head