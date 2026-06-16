class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            count = 1

            for neighbour in adjList[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return True, count
                c, isCycle = dfs(neighbour, node)
                count += c
                if isCycle:
                    return count, True
            
            visited.remove(node)
            return count, False

        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        count, isCycle = dfs(0, None)
        if isCycle or count != n:
            return False
        return True