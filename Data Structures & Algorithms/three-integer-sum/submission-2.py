class Solution:
    def twoSum(self, nums: List[int], current: int):
        left = current + 1
        right = len(nums) - 1
        target = -nums[current]
        pairs = []
        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ == target:
                pairs.append([left, right])
                left += 1
                right -= 1
            elif sum_ > target:
                right -= 1
            else:
                left += 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i, num in enumerate(nums):
            pairs = self.twoSum(nums, i)
            for left, right in pairs:
                result.add((nums[i], nums[left], nums[right]))
        return list(map(lambda x: list(x), result))