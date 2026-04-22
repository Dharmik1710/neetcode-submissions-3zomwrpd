# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        n = len(lists)
        pointer = [None] * n
        for i, p in enumerate(lists):
            pointer[i] = p
        
        while True:
            i, c = 0, 0
            min_, min_i = 1001, None

            while i < n:
                if pointer[i]:
                    if pointer[i].val < min_:
                        min_, min_i = pointer[i].val, i
                else:
                    c += 1

                i+=1
            
            if c == n:
                break
            
            if min_i != None:
                curr.next = pointer[min_i]
                curr = curr.next
                pointer[min_i] = pointer[min_i].next

        return head.next