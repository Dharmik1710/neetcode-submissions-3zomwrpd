class Solution:
    def partition(self, nums: List[int], l: int, r: int) -> int:

        mid = (l + r) >> 1
        if nums[l] < nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        if nums[l+1] < nums[r]:
            nums[l+1], nums[r] = nums[r], nums[l+1]
        if nums[l] < nums[l+1]:
            nums[l], nums[l+1] = nums[l+1], nums[l]
        
        pivot = nums[l+1]
        i = l+1
        j = r

        while True:
            while True:
                i+=1
                if not nums[i] > pivot:
                    break
            
            while True:
                j-=1
                if not nums[j] < pivot:
                    break
            
            if i>j:
                break

            nums[i], nums[j] = nums[j], nums[i]
        
        nums[l+1], nums[j] = nums[j], nums[l+1]
        return j
            
    def quickSelect(self, nums: List[int], k: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            if r <= l+1:
                if r == l+1 and nums[r] > nums[l]:
                    nums[r], nums[l] = nums[l], nums[r]
                return nums[k]

            partitionIdx = self.partition(nums,l,r)
            if partitionIdx > k:
                r = partitionIdx - 1
            elif partitionIdx < k:
                l = partitionIdx + 1
            else:
                return nums[partitionIdx]
        return -1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, k-1)

'''
nums = [2,3,1,5,4], k=3

pivot = 4, 
p=0, i=0, [4,3,1,5,2]
1, 1, [4,3,1,5,2]
2, 2, []
'''
        