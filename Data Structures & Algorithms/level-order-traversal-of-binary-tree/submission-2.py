# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack, tmp = deque(), deque()
        stack.append(root)
        level = []
        while stack:
            node = stack.popleft()
            if not node:
                break
                
            level.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

            if not stack:
                res.append(level)
                stack = tmp
                level = []
                tmp = deque()
        return res


            