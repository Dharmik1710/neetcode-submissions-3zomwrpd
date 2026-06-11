class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        count, t = 0, 0

        visited = set()    
        while q:
            n = len(q)
            i = 0
            while i < n:
                i+=1
                r, c = q.popleft()
                if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == 0:
                    continue
                
                visited.add((r,c))
                if grid[r][c] == 1:
                    t = count 
                    fresh -= 1
                q.append((r-1, c))
                q.append((r+1, c))
                q.append((r, c-1))
                q.append((r, c+1))
            count += 1
        
        return -1 if fresh else t
