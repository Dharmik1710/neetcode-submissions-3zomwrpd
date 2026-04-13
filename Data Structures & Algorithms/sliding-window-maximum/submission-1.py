import heapq

class SegmentTree:
    def __init__(self, N, nums) -> None:
        self.n = N
        while self.n & (self.n - 1):
            self.n += 1
        self.build(N, nums)

    def build(self, N, nums) -> None:
        self.tree = [float('-inf')] * (2 * self.n)
        for i in range(N):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i<<1], self.tree[i<<1 | 1])

    def query(self, l, r) -> int:
        l += self.n
        r += self.n
        max_ = float('-inf')
        while(l < r):
            if l & 1:
                max_ = max(max_, self.tree[l])
                l += 1
            if r & 1 > 0:
                r -= 1
                max_ = max(max_, self.tree[r])
            l >>= 1
            r >>= 1
        return max_

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = SegmentTree(len(nums), nums)
        res = []
        for i in range(len(nums) - k + 1):
            window_max = st.query(i, i+k)
            res.append(window_max)
        return res