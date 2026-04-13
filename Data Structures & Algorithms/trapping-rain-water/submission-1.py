class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        left, right = [], []
        left_max, right_max = 0, 0
        i = 0
        while(i < n):
            right_max = max(right_max, height[n - i - 1])
            left_max = max(left_max, height[i])
            left.append(left_max)
            right.append(right_max)
            i += 1
        i = 0
        while i < n:
            total += min(left[i], right[n - i - 1]) - height[i]
            i += 1
        return total
            