class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        while abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                n = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -n)
            else:
                n = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -n)
        
    def findMedian(self) -> float:
        print(self.maxHeap)
        print(self.minHeap)
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]

'''
odd:[1,2,3]
if new number not added to left; current_med_idx+=1

even:[1,2,3,4]
if new num added to left or at cur med; current_med_idx -= 1
'''