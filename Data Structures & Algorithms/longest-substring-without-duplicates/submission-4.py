class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        hm = {}
        max_ = 0
        while end < len(s):
            if s[end] in hm:
                max_ = max(max_, end - start)
                start = max(start, hm[s[end]] + 1)
            hm[s[end]] = end
            end += 1
        return max(max_, end - start)