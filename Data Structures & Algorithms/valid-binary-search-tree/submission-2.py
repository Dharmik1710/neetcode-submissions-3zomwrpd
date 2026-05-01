# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], l=-float('inf'), r=float('inf')) -> bool:
        if not root:
            return True
        
        if root.val <= l or root.val >= r:
            return False
        
        return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val, r)