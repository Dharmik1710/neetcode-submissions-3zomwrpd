class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        max_=0
        for num in nums:
            if num - 1 not in s:
                count = 1
                while num + count in s:
                    count += 1
                max_=max(max_, count)
        return max_