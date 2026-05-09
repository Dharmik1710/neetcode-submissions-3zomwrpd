from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. Count and sort unique candidates
        d = Counter(candidates)
        unique_nums = sorted(d.keys())
        n = len(unique_nums)

        def dfs(i, cur_target, subset):
            if cur_target == 0:
                res.append(subset.copy())
                return
            if i == n:
                return

            num = unique_nums[i]

            # 2. Early Pruning: If the smallest available number is too big, 
            # no need to explore this branch or any skip branches at this level.
            if num <= cur_target:
                # 3. Batching: Decide how many of unique_nums[i] to use
                count = d[num]
                for use_count in range(1, count + 1):
                    if num * use_count <= cur_target:
                        subset.append(num)
                        dfs(i + 1, cur_target - (num * use_count), subset)
                    else:
                        break
                
                # Backtrack: remove all instances added in this loop
                for _ in range(len(subset)):
                    if subset[-1] == num:
                        subset.pop()
                    else:
                        break

            # 4. Skip branch
            dfs(i + 1, cur_target, subset)

        dfs(0, target, [])
        return res
