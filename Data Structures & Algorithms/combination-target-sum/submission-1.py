class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, sum_):
            if sum_ > target or i >= len(nums):
                return
            if sum_ == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i, sum_ + nums[i])
            subset.pop()
            dfs(i+1, sum_)

        dfs(0, 0)    
        return list(res)

'''

'''