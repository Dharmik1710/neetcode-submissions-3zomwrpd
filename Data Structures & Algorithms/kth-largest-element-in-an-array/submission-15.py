import heapq
import random

class Solution:
    def getPivotIdx(self, nums, l, r) -> int:
        m = (l+r) >> 1
        if nums[l] >= nums[m] >= nums[r] or nums[l] <= nums[m] <= nums[r]:
            return m
        elif nums[m] >= nums[l] >= nums[r] or nums[m] <= nums[l] <= nums[r]:
            return l
        else:
            return r

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivotIdx = self.getPivotIdx(nums, l, r)
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
        