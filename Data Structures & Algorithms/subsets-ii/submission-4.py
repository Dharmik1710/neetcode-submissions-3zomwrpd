from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subset = []
        d = Counter(nums)
        uniq = list(d.keys())

        def backtrack(i):
            if i >= len(uniq):
                # res.append(subset.copy())
                return
            
            if d[uniq[i]] > 0:
                subset.append(uniq[i])
                d[uniq[i]] -= 1
                res.append(subset.copy())
                backtrack(i)
                subset.pop()
                d[uniq[i]] += 1
            
            backtrack(i+1)
        
        backtrack(0)
        return res