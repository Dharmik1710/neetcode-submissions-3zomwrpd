class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [], []
        max_ = 0
        total = 0
        for h in height:
            max_ = max(max_, h)
            left.append(max_)
        max_ = 0
        for h in height[::-1]:
            max_ = max(max_, h)
            right.append(max_)
        i = 0
        while i < n:
            total += min(left[i], right[n - i - 1]) - height[i]
            i += 1
        return total
            