import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        d = Counter(tasks)
        cooldown = [0]*26
        maxHeap = [[-val, key] for key, val in d.items()]
        heapq.heapify(maxHeap)

        cycles = 0
        executed = 0
        while executed < len(tasks):
            cycles += 1
            
            min_cooldown = float('inf')
            for i, t in enumerate(cooldown):
                if t == 0:
                    continue
                if cycles > t:
                    task = chr(ord('A') + i)
                    if d[task] > 0:
                        heapq.heappush(maxHeap, [-d[task], task])
                    cooldown[i] = 0
                else:
                    min_cooldown = min(min_cooldown, t)
            
            if maxHeap:
                count, task = heapq.heappop(maxHeap)
                executed += 1
                d[task] -= 1
                cooldown[ord(task) - ord('A')] = cycles + n
            else:
                cycles = min_cooldown
            
        return cycles