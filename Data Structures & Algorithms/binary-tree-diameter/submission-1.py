# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        stack = [root]
        mp = {None: -1}

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
            
                height = max(mp[node.left], mp[node.right]) + 1
                diameter = max(diameter, mp[node.left] + mp[node.right] + 2)

                mp[node] = height
        
        return diameter
            
            
