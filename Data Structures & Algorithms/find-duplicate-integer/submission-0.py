class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            n = nums[i]-1
            if i != n:
                if nums[i] == nums[n]:
                    return nums[i]
                else:
                    nums[i], nums[n] = nums[n], nums[i]
                    continue
            i += 1 
            

        return res