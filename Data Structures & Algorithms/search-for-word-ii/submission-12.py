class Node:
    def __init__(self):
        self.end = False
        self.letters = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def trie(word: str, t: Node) -> None:
            for ch in word:
                if ch not in t.letters:
                    t.letters[ch] = Node()
                t = t.letters[ch]
            t.end = True

        def search(t: Node, r: int, c: int, l: List[str]) -> None:
            if r < 0 or c < 0 or r == rows or c == cols or visited[r][c] or board[r][c] not in t.letters:
                return

            visited[r][c] = True
            l.append(board[r][c])
            t = t.letters[board[r][c]]
            if t.end:
                res.add("".join(l))
            search(t, r-1, c, l) 
            search(t, r+1, c, l)
            search(t, r, c-1, l)
            search(t, r, c+1, l)
            l.pop()
            visited[r][c] = False
            return
        
        def dfs() -> bool:
            for r in range(rows):
                for c in range(cols):
                    search(t, r, c, [])
            return False

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        res = set()
        t = Node()
        for word in words:
            trie(word, t)
        
        dfs()
        return list(res)