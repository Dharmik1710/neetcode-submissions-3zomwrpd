class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, WORD_LEN = len(board), len(board[0]), len(word)

        def dfs(i: int, j: int, k: int) -> bool:
            
            if k == WORD_LEN:
                return True

            if i < 0 or j < 0 or i == ROWS or j == COLS or (i, j) in visited or board[i][j] != word[k]:
                return False
            
            visited.add((i, j))
            tmp = dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            visited.remove((i, j))
            return tmp
        
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
            

'''
a b c e
s f e s
a d e e

abceseeefs

'''