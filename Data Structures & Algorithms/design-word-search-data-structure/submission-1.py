from collections import deque

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not current.children[i]:
                current.children[i] = Node()
            current = current.children[i]
        current.endword = True

    def search(self, word: str) -> bool:
        q = deque()
        q.append(self.root)
        for char in word:
            size = len(q)
            while size:
                current = q.popleft()
                if char == '.':
                    for i in current.children:
                        if i:
                            q.append(i)
                else:
                    i = ord(char) - ord('a')
                    if current.children[i]:
                        q.append(current.children[i])
            
                size -= 1
            
            if not len(q):
                return False
        
        while q:
            if q.popleft().endword:
                return True

        return False
            
            
            