class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_ = 0
        while left < right:
            max_ = max((right - left) * min(heights[right], heights[left]), max_)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_