import heapq

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        for i in range(len(nums)):
            # Add kth element to max heap
            heapq.heappush(max_heap, (-nums[i], i))

            if i - k + 1 >= 0:
                # while root not in window[i, i+k], remove the root
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)

                res.append(-max_heap[0][0])
        return res