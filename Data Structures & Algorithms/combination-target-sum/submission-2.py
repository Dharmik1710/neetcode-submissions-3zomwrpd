class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i, sum_):
            if sum_ > target or i >= len(nums) or nums[i] > target:
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