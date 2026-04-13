class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        begin = []
        for num in nums:
            if num - 1 not in s:
                begin.append(num)
        max_=0
        for num in begin:
            count = 1
            while(count < len(nums)):
                num += 1
                if num not in s:
                    break
                count += 1
            max_=max(max_, count)
        return max_