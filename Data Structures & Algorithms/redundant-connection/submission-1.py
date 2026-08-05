class DSU:
    def __init__(self, n):
        self.rank = [1]*(n+1)
        self.tree = [i for i in range(n+1)]
        self.edge = None
    
    def find(self, n):
        if self.tree[n] == n:
            return n
        return self.find(self.tree[n])
    
    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            self.edge = [a, b]
            return

        if self.rank[ap] > self.rank[bp]:
            self.rank[ap] += self.rank[bp]
            self.tree[bp] = ap
        else:
            self.rank[bp] += self.rank[ap]
            self.tree[ap] = bp

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for a, b in edges:
            dsu.union(a, b)
        
        return dsu.edge
        