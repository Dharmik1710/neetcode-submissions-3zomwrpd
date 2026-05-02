# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max = -float('inf')
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            self.max = max(self.max, root.val + left + right)
            return max(left, right) + root.val
        
        dfs(root)
        return self.max

'''
root    left    right   self.max
1       2       3       0
2       0       0       2
3       0       0       3
'''
