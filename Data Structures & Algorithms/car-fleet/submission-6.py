class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted([list(item) for item in zip(position, speed)], reverse=True)
        res = 0
        prev = float('-inf')
        for p, s in sorted_pos:
            cur = (target - p) / s
            if cur > prev:
                res += 1
                prev = cur
        return res