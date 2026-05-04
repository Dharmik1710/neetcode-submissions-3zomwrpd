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
        stack = []
        current = root
        l = []

        while stack or current:
            while current:
                stack.append(current)
                l.append(f'{current.val}')
                current = current.left
            
            l.append('N')
            node = stack.pop()
            current = node.right

        return ",".join(l)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if not data or data =='N':
            return None

        l = data.split(",")
        root = TreeNode(l[0])
        prev = root
        stack = [root]

        i = 1
        while i<len(l):
            while i<len(l) and l[i] != 'N':
                prev.left = TreeNode(int(l[i]))
                prev = prev.left
                stack.append(prev)
                i+=1
                
            node = stack.pop()
            i+=1
            if i<len(l) and l[i] != 'N': 
                prev = node.right = TreeNode(int(l[i]))
                stack.append(prev)
                i+=1

        return root


        

'''
level order
1#  $  2#  3#   $   &   &   4#  5#  $

'''