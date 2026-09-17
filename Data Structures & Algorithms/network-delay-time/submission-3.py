class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        l = [float('inf')]*(n+1)
        l[k] = 0
        adj_list = defaultdict(list)
        visited = set()

        # Adj list
        for from_, to_, time in times:
            adj_list[from_].append([to_, time])
        
        hq = [[0, k]]
        max_ = 0

        # Djistras algorithm
        while hq:
            time, node = heapq.heappop(hq)
            if node in visited:
                continue
            visited.add(node)
            max_ = max(max_, time)

            for adj_node, t in adj_list[node]:
                heapq.heappush(hq, [time+t, adj_node])
        
        return max_ if len(visited) == n else -1