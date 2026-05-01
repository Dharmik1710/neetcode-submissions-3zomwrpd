# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def checkNodes(root: TreeNode, max_: int) -> None:
            nonlocal count
            if not root:
                return
            if root.val >= max_:
                count += 1
                max_ = root.val
            
            checkNodes(root.left, max_)
            checkNodes(root.right, max_)
        
        if root:
            checkNodes(root, root.val)
        return count

            
        