"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        def dfsClone(node: Optional['Node']) -> None:            
            visited.add(node)
            for n in node.neighbors:
                if n in visited:
                    continue
                dfsClone(n)
            node.neighbors.append(Node(node.val))
        
        def addNeighbors(node: Optional['Node']) -> None:
            visited.add(node)
            node_copy = node.neighbors[-1]
            for n in node.neighbors[:-1]:
                node_copy.neighbors.append(n.neighbors[-1])
                if n in visited:
                    continue
                addNeighbors(n)
        
        def popCopy(node: Optional) -> Optional['Node']:
            visited.add(node)
            cloned_node = node.neighbors.pop()
            for n in node.neighbors:
                if n in visited:
                    continue
                popCopy(n)
            
            return cloned_node
        
        visited = set()
        dfsClone(node)
        visited.clear()
        addNeighbors(node)
        visited.clear()
        return popCopy(node)