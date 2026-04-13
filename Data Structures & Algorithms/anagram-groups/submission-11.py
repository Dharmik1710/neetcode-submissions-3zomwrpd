from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            l = [0]*26
            for i in s:
                l[ord(i) - ord('a')] += 1
            k = " ".join(map(str, l))
            res[k].append(s)
        return list(res.values())
            