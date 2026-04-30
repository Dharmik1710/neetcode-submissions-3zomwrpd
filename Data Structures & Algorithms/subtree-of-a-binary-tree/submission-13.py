# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "$"
        
        return f"#{root.val}#{self.serialize(root.left)}#{self.serialize(root.right)}"

    def zfunction(self, s: str) -> list:
        z = [0]
        n = len(s)
        l, r, i = 1, 1, 1
        while i < n:
            while r < n and s[r] == s[r-l]:
                r+=1
            z.append(r-l)
            i+=1
            while i < n and i < r:
                if i + z[i-l] >= r:
                    break
                z.append(z[i-l])
                i+=1
            l = i
            if r < l:
                r = l
        return z
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rs = self.serialize(root)
        srs = self.serialize(subRoot)
        
        # s = "aabxaabxcaabxaabxay"
        z = self.zfunction(srs + "|" + rs)
        # z = self.zfunction(s)

        return len(srs) in z
