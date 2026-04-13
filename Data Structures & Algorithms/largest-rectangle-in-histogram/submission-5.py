class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_ = 0
        n = len(heights)
        i = 0
        left, right = [0] * n, [0] * n
        ls, rs = [], []
        lref, rref = None, None
        while i < n:
            while rs and heights[rs[-1]] > heights[i]:
                ind = rs.pop()
                right[ind] = i - ind - 1
            while ls and heights[ls[-1]] > heights[n - i - 1]:
                ind = ls.pop()
                left[ind] = (ind - (n - i))
            rs.append(i)
            ls.append(n-i-1)
            i+=1
        while ls:
            if lref == None:
                lref = ls[-1]
            ind = ls.pop()
            left[ind] = ind - lref
        while rs:
            if rref == None:
                rref = rs[-1]
            ind = rs.pop()
            right[ind] = rref - ind
        for i, h in enumerate(heights):
            rec_area = (left[i] + right[i] + 1) * h
            max_=max(max_, rec_area)
        return max_

            