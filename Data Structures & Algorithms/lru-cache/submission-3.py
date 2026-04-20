from collections import OrderedDict

class Node:
    def __init__(self, k: int = 0, v: int = 0):
        self.val = v

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
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
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
        
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)