class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        col, pos, neg = 0, 0, 0

        def backtracking(r: int, queen: List[int]):
            nonlocal col, pos, neg
            if r == n:
                res.append(['.'*c + 'Q' + '.'*(n-c-1) for c in queen])
                return

            for c in range(n):
                if (1 << c & col) or (1 << (c+r) & pos) or (1 << (c-r+n) & neg):
                    continue
                
                col ^= (1 << c)
                pos ^= 1 << (c+r)
                neg ^= 1 << (c-r+n)
                queen.append(c)
                
                backtracking(r+1, queen)
                
                col ^= (1 << c)
                pos ^= 1 << (c+r)
                neg ^= 1 << (c-r+n)
                queen.pop()
        
        backtracking(0, [])
        return res