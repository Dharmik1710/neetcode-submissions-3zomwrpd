from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        
        visited = set()
        while q:
            n = len(q)
            i = 0
            while i < n:
                i+=1
                r, c, d = q.popleft()
                if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1 or (r, c) in visited:
                    continue
                
                visited.add((r, c))
                grid[r][c] = min(grid[r][c], d)
                q.append((r-1, c, d+1))
                q.append((r+1, c, d+1))
                q.append((r, c-1, d+1))
                q.append((r, c+1, d+1))