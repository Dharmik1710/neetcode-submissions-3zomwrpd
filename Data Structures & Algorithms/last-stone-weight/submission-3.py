class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = max(stones)
        buckets = [0] * (n+1)
        for stone in stones:
            buckets[stone] += 1
        remainder = 0
        while n > 0:
            if buckets[n]:
                if remainder:
                    x = min(math.floor(remainder/n), buckets[n])
                    remainder -= (n * x)
                    buckets[remainder] += 1
                    buckets[n] -= x
                
                if remainder < n:
                    remainder = (buckets[n]%2) * n
            n-=1
        return remainder




        

'''
sort - nlogn + n(logn + n) 

heap - n + nlogn

[2,3,6,2,4] -> (6-4), [6,4,3,2,2] -> (3-2)[3,2,2,2] -> (2-2)[2,2,1] -> 1
[2,3,6,2,4] -> [1,3,4,2] -> []


'''