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
        q = deque()
        q.append(root)
        l = []

        while q:
            n = len(q)
            
            node = q.popleft()
            if node:
                l.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                l.append("N")
        return ",".join(l)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data =="N":
            return None

        l = data.split(",")
        current = TreeNode(l[0])
        q = deque()
        q.append(current)

        i = 1
        while i < len(l):
            node = q.popleft()
            if l[i] != "N":
                node.left = TreeNode(int(l[i]))
                q.append(node.left)
            i+=1
            if i < len(l) and l[i] != "N":
                node.right = TreeNode(int(l[i]))
                q.append(node.right)
            i+=1            

        return current


        

'''
level order
1#  $  2#  3#   $   &   &   4#  5#  $

'''