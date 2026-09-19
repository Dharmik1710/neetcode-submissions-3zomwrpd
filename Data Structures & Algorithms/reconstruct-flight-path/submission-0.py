class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        res = []

        # adj list
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
                
        # DFS
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]

