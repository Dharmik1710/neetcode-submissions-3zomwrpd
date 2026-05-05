import heapq
import random

class Solution:
    def partition(self, nums: List[int]) -> int:
        pass


    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivotIdx = random.randint(l, r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
            
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[r], nums[p] = nums[p], nums[r]

            if p>k:
                return quickSelect(l, p-1)
            elif p<k:
                return quickSelect(p+1, r)
            else:
                return nums[p]    

        return quickSelect(0, len(nums)-1)
    


'''
nums = [2,3,1,5,4], k=3

pivot = 4, 
p=0, i=0, [4,3,1,5,2]
1, 1, [4,3,1,5,2]
2, 2, []
'''
        