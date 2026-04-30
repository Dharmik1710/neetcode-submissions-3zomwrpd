# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            v = None
            for i in range(n):
                node = q.popleft()
                if node:
                    v = node.val
                    q.append(node.left)
                    q.append(node.right)
            if v:
                l.append(v)
        return l