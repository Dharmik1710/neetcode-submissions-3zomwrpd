class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            indegrees[b] += 1
            adj_list[a].append(b)
        
        q = deque()
        for i, n in enumerate(indegrees):
            if n == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            for pre in adj_list[course]:
                indegrees[pre] -= 1
                if indegrees[pre] == 0:
                    q.append(pre)
        
        for i in indegrees:
            if i:
                return False

        return True