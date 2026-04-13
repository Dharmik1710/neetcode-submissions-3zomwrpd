class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        sorted_piles = sorted(piles, reverse=True)
        l, r = 1, sorted_piles[0]
        res = r
        
        while l <= r:
            m = (l+r)//2

            j = 0
            total = 0
            while j < n and sorted_piles[j] > m:
                total += math.ceil(sorted_piles[j]/m)
                j+=1
            total += (n - j)

            if total <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
