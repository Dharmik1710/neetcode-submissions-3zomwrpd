class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'{': '}', '[': ']', '(': ')'}
        for ch in s:
            if ch in d:
                stack.append(ch)
            else:
                if not stack or ch != d[stack.pop()]:
                    return False
        return stack == []