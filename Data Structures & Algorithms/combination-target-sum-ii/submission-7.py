from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        d = Counter(candidates)
        candidates = list(set(candidates))

        def dfs(i, sum_):
            if sum_ == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or sum_ > target:
                return
            
            if d[candidates[i]] > 0:
                subset.append(candidates[i])
                d[candidates[i]] -= 1
                dfs(i, sum_ + candidates[i])
                d[candidates[i]] += 1
                subset.pop()
            dfs(i+1, sum_)
            
        
        dfs(0, 0)
        return res
