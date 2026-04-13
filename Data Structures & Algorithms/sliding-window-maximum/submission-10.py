class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l2r_max = []
        r2l_max = []
        n = len(nums)
        i = 0
        while i < math.ceil(n/k):
            l2r = []
            r2l = []
            j = 0
            l_max, r_max = float('-inf'), float('-inf')
            num_elements = min(k, n - i*k)
            while j < num_elements:
                l = i*k + j
                r = i*k + num_elements - j - 1
                l_max = max(l_max, nums[l])
                r_max = max(r_max, nums[r])
                l2r.append(l_max)
                r2l.append(r_max)
                j += 1
            l2r_max.append(l2r)
            r2l_max.append(r2l)
            i += 1
        
        i = 0
        while i <= n - k:
            l, r = i, i+k-1
            l_max = r2l_max[l//k][k - (l%k + 1)]
            r_max = l2r_max[r//k][r%k]
            res.append(max(l_max, r_max))
            i+=1
        return res


            