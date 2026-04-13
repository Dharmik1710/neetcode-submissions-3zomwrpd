class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        result = []
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        sorted_hm = sorted(hm.items(), key=lambda item: item[1], reverse= True)
        return list(map(lambda x: x[0], sorted_hm[:k]))             