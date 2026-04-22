# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while left or right:
            if left and not right:
                curr.next = left
                break
            
            if right and not left:
                curr.next = right
                break

            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        if n == 1:
            return lists[0]
        
        m = n//2
        left = self.mergeKLists(lists[:m])
        right = self.mergeKLists(lists[m:])

        return self.merge(left, right)