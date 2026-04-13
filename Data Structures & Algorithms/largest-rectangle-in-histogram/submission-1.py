class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_ = 0
        i = 0
        while i < len(heights):
            n = 0
            while stack and stack[-1][0] >= heights[i]:
                n+=1
                height, prev = stack.pop()
                n+=prev
                max_ = max(max_, n * height)
            
            stack.append((heights[i], n))
            i+=1

        n = 0
        while stack:
                n+=1
                height, prev = stack.pop()
                max_ = max(max_, (prev + n) * height)
        return max_
