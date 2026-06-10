"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def dfsClone(node: Optional['Node']) -> None:
            if not node or node in visited:
                return
            
            visited.add(node)
            for n in node.neighbors:
                dfsClone(n)
            node.neighbors.append(Node(node.val))
        
        def addNeighbors(node: Optional['Node']) -> None:
            if not node or node in visited:
                return
            
            visited.add(node)
            node_copy = node.neighbors[-1]
            for n in node.neighbors[:-1]:
                node_copy.neighbors.append(n.neighbors[-1])
                addNeighbors(n)
        
        def popCopy(node: Optional) -> Node:
            if not node or node in visited:
                return
            
            visited.add(node)
            for n in node.neighbors[:-1]:
                popCopy(n)
            
            return node.neighbors.pop()
        
        visited = set()
        dfsClone(node)
        visited.clear()
        addNeighbors(node)
        visited.clear()
        return popCopy(node)