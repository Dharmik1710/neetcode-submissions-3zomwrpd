class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for n in nums:
            k = len(res)-1
            while k >= 0:
                cpy = res[k].copy()
                cpy.append(n)
                res.append(cpy)
                k-=1
        return res