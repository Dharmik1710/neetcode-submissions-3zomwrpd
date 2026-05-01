# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def checkNodes(root: TreeNode, max_: int, count: int) -> None:
            if not root:
                return 0
            if root.val >= max_:
                count += 1
                max_ = root.val
            
            count += checkNodes(root.left, max_, 0)
            count += checkNodes(root.right, max_, 0)
            return count
        
        return checkNodes(root, root.val, 0)

            
        