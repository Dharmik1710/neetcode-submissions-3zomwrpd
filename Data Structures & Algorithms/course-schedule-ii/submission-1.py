class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        adj_list = {i: [] for i in range(numCourses)}
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adj_list[a].append(b)
            indegrees[b] += 1
        
        q = deque()
        for i, n in enumerate(indegrees):
            if n == 0:
                q.append(i)
        
        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            res.append(course)
            for pre in adj_list[course]:
                indegrees[pre] -=1
                if indegrees[pre] == 0:
                    q.append(pre)

        res.reverse()     
        return res if finish == numCourses else []