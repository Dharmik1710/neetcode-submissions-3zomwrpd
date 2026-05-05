import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxHeap = []
        heapq.heapify(maxHeap)
        mp = defaultdict(list)
        for (i, j) in points:
            distance = i**2 + j**2
            mp[distance].append([i,j])
            heapq.heappush(maxHeap, -distance)
            if len(maxHeap) > k:
                dist = -heapq.heappop(maxHeap)
                mp[dist].pop()
        for pts in mp.values():
            res.extend(pts)
        return res