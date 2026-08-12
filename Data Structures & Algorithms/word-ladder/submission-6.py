class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def generate(word):
            l = set()
            for i in range(len(word)):
                nw = list(word)
                for j in range(26):
                    nw[i] = chr(ord("a") + j)
                    l.add("".join(nw))
            return l

        q = deque()
        q.append((beginWord, 1))
        visited = set()
        
        while q:
            cw, count = q.popleft()
            visited.add(cw)
            parents = generate(cw)
            # print(parents)
            # print(visited)
            # print(cw, count)
            for word in wordList:
                if word in visited:
                    continue
                if word in parents:
                    q.append((word, count+1))
                    if word == endWord:
                        return count+1
        return 0