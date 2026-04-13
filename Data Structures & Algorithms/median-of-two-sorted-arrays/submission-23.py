class Solution:
    
    def kthSmallest(self, nums1: List[int], nums2: List[int], k: int) -> int:
        kby2 = k//2
        if len(nums1) < kby2 or len(nums1) == 0:
            return nums2[k - len(nums1) - 1]
        if len(nums2) < kby2 or len(nums2) == 0:
            return nums1[k - len(nums2) - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        if nums1[kby2-1] < nums2[kby2-1]:
            return self.kthSmallest(nums1[kby2:], nums2, k-kby2)
        else:
            return self.kthSmallest(nums1, nums2[kby2:], k-kby2)

    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        is_even = (n+m)%2 == 0
        median = self.kthSmallest(nums1, nums2, (n+m)//2 + 1)
        if is_even:
            median += self.kthSmallest(nums1, nums2, (n+m)//2)
        return median/2 if is_even else median