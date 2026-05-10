from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = deque()
        permutations.append([])

        for n in nums:
            l = len(permutations)
            while l > 0:
                l-=1
                p = permutations.popleft()
                for i in range(len(p) + 1):
                    tmp = p.copy()
                    tmp.insert(i, n)
                    permutations.append(tmp)
        return list(permutations)