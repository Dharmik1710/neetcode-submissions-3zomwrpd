class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted([list(item) for item in zip(position, speed)], reverse=True)
        stack = []
        for p, s in sorted_pos:
            t = (target - p) / s
            stack.append(t)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)