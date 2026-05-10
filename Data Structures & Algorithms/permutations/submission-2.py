from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(nums: List[int], idx: int) -> None:
            if idx == len(nums):
                permutations.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            
        backtrack(nums, 0)
        return permutations