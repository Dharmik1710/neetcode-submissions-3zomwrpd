import queue

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_ = 0
        l, r = 0, 0
        freq = {}
        while r < len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            
            freq_char = max(freq, key=freq.get)
            while l < r and k < (r - l + 1) - freq[freq_char]:
                freq[s[l]] -= 1
                l += 1
                freq_char = max(freq, key=freq.get)
            max_ = max(max_, r - l + 1)
            r += 1
        return max_