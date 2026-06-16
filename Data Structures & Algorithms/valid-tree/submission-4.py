class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited or dfs(neighbour, node):
                    return True
                
            return False

        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        return False if dfs(0, None) or len(visited) != n else True