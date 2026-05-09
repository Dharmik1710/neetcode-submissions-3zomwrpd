class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i, sum_):
            if sum_ == 0:
                res.append(subset.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] > sum_:
                    return
                
                subset.append(nums[j])
                dfs(j, sum_ - nums[j])
                subset.pop()

        dfs(0, target)
        return res