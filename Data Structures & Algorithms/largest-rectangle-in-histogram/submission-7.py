class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                tmp_i, tmp_h = stack.pop()
                res = max(res, tmp_h * (i - tmp_i))
                start = tmp_i
            
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i)) 

        return res

            