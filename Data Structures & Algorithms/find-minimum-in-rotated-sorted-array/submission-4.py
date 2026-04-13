class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1001
        l , r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            res = min(res, nums[m])
            if l == r:
                break
            if nums[l] > nums[r]:
                if nums[l] > nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                r = m-1
        return res