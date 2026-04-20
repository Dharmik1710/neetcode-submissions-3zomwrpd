class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for b in range(32):
            mask = 1 << b
            
            x = 0
            for n in nums:
                x += (n & mask)
            
            y = 0
            for n in range(1, len(nums)):
                y += (n & mask)
            
            if x > y:
                res = res | mask

        return res