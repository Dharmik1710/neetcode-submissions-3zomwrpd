class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        col, pos = set(), set()
        neg = set()

        def backtracking(r: int, queen: List[int]):
            if r == n:
                res.append(['.'*c + 'Q' + '.'*(n-c-1) for c in queen])
                return

            for c in range(n):
                if not (c in col or (c+r) in pos or (c-r) in neg):
                    col.add(c)
                    pos.add(c+r)
                    neg.add(c-r)
                    queen.append(c)
                    
                    backtracking(r+1, queen)
                    
                    col.remove(c)
                    pos.remove(c+r)
                    neg.remove(c-r)
                    queen.pop()
        
        backtracking(0, [])
        return res