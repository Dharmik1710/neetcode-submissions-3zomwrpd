class Node:
    def __init__(self, letter: str = None, flag: bool = False) -> None:
        self.letter = letter
        self.nextNode = [None] * 26
        self.flag = flag

class PrefixTree:

    def __init__(self):
        self.letters = Node()

    def insert(self, word: str) -> None:
        if not word:
            return

        i = 0
        prev = self.letters
        for char in word:
            cur = prev.nextNode[ord(char) - ord('a')]
            if not cur:
                cur = Node(char)
                prev.nextNode[ord(char) - ord('a')] = cur

            prev = cur
            i+=1
        
        prev.flag = True

    def search(self, word: str) -> bool:
        prev = self.letters
        for char in word:
            prev = prev.nextNode[ord(char) - ord('a')]
            if not prev:
                return False
        
        return prev.flag

    def startsWith(self, prefix: str) -> bool:
        prev = self.letters
        for char in prefix:
            prev = prev.nextNode[ord(char) - ord('a')]
            if not prev:
                return False
        
        return True
        