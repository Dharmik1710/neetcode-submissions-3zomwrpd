class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(node: int) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            courses[node] = True
            for n in adj_list[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            
            return True
        
        adj_list = defaultdict(list)
        visited = set()
        courses = [False] * numCourses
        for a, b in prerequisites:
            adj_list[a].append(b)
        
        for node in range(numCourses):
            if courses[node]:
                continue
            if not dfs(node):
                return False
        return True