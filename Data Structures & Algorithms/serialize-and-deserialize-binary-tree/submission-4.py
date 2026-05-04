# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        l = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                l.append('N')
                return
            l.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(l)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if not data or data =='N':
            return None
        
        
        l = data.split(",")
        self.i = 0

        def dfs():
            if l[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(l[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
            

        return dfs()


        

'''
level order
1#  $  2#  3#   $   &   &   4#  5#  $

'''