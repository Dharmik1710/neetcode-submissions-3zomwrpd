class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        ns1, ns2 = len(s1), len(s2)
        s1hm, s2hm = {}, {}
        for i in range(ns1):
            s1hm[s1[i]] = s1hm.get(s1[i], 0) + 1
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1
        
        if s1hm == s2hm:
            return True

        for i in range(ns1, ns2):
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1
            s2hm[s2[i - ns1]] -= 1
            count = 0
            for ch in s1:
                if ch in s2hm and s2hm[ch] == s1hm[ch]:
                    count += 1
            if count == ns1:
                return True

        return False