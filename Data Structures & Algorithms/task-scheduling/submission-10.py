import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cooldown = deque()
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)

        cycles = 0
        while maxHeap or cooldown:
                
            if maxHeap:
                cycles += 1
                task = -heapq.heappop(maxHeap)
                if task > 1:
                    cooldown.append((task-1, cycles+n))
            else:
                cycles = cooldown[0][1]
            
            if cooldown:
                if cooldown[0][1] == cycles:
                    heapq.heappush(maxHeap, -cooldown.popleft()[0])
            
        return cycles