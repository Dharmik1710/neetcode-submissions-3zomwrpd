class Dsu:
    def __init__(self, n):
        self.tree = [i for i in range(n)]
        self.rank = [1]*n
        self.count = n

    def findParent(self, n):
        if self.tree[n] == n:
            return n
        return self.findParent(self.tree[n])
    
    def union(self, a, b):
        ap = self.findParent(a)
        bp = self.findParent(b)
        if ap == bp:
            return
        if self.rank[ap] > self.rank[bp]:
            self.rank[ap] += self.rank[bp]
            self.tree[bp] = ap
        else:
            self.rank[bp] += self.rank[ap]
            self.tree[ap] = bp
        self.count -= 1

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsuObj = Dsu(n)
        for a, b in edges:
            dsuObj.union(a, b)
        
        return dsuObj.count