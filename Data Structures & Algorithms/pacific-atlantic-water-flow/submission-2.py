class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r: int, c: int, ocean: Set[[int, int]]) -> None:
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in ocean:
                return
            
            ocean.add((r,c))
            if r-1 >= 0 and heights[r][c] <= heights[r-1][c]:
                dfs(r-1, c, ocean)
            if r+1 < rows and heights[r][c] <= heights[r+1][c]:
                dfs(r+1, c, ocean)
            if c-1 >= 0 and heights[r][c] <= heights[r][c-1]:
                dfs(r, c-1, ocean)
            if c+1 < cols and heights[r][c] <= heights[r][c+1]:
                dfs(r, c+1, ocean)
                            
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)
        
        # for r, c in pacific.copy():
        #     dfs(r, c, pacific)
        # for r, c in atlantic.copy():
        #     dfs(r, c, atlantic)
            
        return list(pacific & atlantic)