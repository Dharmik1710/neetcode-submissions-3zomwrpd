# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root: Optional[TreeNode]) -> (int, int):
        max_ = 0
        if not root:
            return (0, 0)
        
        left_height, left_d = self.maxHeight(root.left, )
        right_height, right_d = self.maxHeight(root.right)

        max_ = max(left_d, right_d, left_height + right_height)
        return (max(left_height, right_height) + 1, max_)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.maxHeight(root)[-1]