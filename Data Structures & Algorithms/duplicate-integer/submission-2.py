class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            d[num] = True
        if len(d) == len(nums):
            return False
        return True
