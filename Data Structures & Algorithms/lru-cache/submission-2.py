class Node:
    def __init__(self, k: int = 0, v: int = 0):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.right = Node()
        self.left = Node()
        self.right.prev = self.left
        self.left.next = self.right
        
        self.cache = {}
        self.size = capacity
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _addRight(self, node):
        tmp = self.right.prev
        tmp.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = tmp

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._addRight(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._addRight(node)
        self.cache[key] = node
        
        if len(self.cache) > self.size:
            node = self.left.next
            self._remove(node)
            del self.cache[node.key]