# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i, node in enumerate(inorder):
            mp[node] = i
        
        def build(l: int, r: int, rootIndex:int) -> Optional[TreeNode]:
            print(l, r, rootIndex)     
            if l > r:
                return None
            
            
            root = preorder[rootIndex]
            rootNode = TreeNode(root)
            if l == r:
                return rootNode
            
            rootNode.left = build(l, mp[root]-1, rootIndex+1)
            rootNode.right = build(mp[root]+1, r, rootIndex + mp[root] - l + 1)
            return rootNode
        
        return build(0, len(preorder)-1, 0)