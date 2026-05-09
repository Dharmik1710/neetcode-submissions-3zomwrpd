class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        i = 0
        while i < len(nums):
            j = 0
            k = len(res)
            while j < k:
                cpy = res[j].copy()
                cpy.append(nums[i])
                res.append(cpy)
                j+=1
            i+=1
        return res