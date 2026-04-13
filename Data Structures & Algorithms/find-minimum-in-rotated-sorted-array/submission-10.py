class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l , r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < res:
                    res = nums[l]
                break
            else:
                m = (l+r)//2
                if nums[l] <= nums[m]:
                    if nums[l] < res:
                        res = nums[l]
                    l = m+1
                elif nums[m] <= nums[r]:
                    if nums[m] < res:
                        res = nums[m]
                    r = m-1
        return res