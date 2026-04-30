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
        while q and root:
            n = len(q)
            v = None
            for i in range(n):
                node = q.popleft()
                v = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l.append(v)
        return l