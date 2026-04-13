class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        median = []
        is_even = (n+m)%2 == 0
        med_ind = (n+m)//2
        while i+j < m+n:
            ci, cj = float('inf'), float('inf')
            if i < m:
                ci = nums1[i]
            if j < n:
                cj = nums2[j]
            
            if is_even:
                if i+j == med_ind or i+j == med_ind-1:
                    median.append(min(ci, cj))
            else:
                if i+j == med_ind:
                    median.append(min(ci, cj))
            
            if ci < cj:
                i+=1
            else:
                j+=1
        return sum(median)/len(median)

