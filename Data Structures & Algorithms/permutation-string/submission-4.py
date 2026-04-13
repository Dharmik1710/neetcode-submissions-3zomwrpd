class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        ns1, ns2 = len(s1), len(s2)
        s1hm, s2hm = {}, {}
        for i in range(ns1):
            s1hm[s1[i]] = s1hm.get(s1[i], 0) + 1
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1

        count = 0
        for ch in s1:
            if ch in s2hm and s2hm[ch] == s1hm[ch]:
                count += 1

        for i in range(ns1, ns2):
            if count == len(s1hm):
                return True
            
            if s2[i - ns1] in s1hm and s2hm[s2[i - ns1]] == s1hm[s2[i - ns1]]:
                count -= 1
            s2hm[s2[i - ns1]] -= 1
            if s2[i - ns1] in s1hm and s2hm[s2[i - ns1]] == s1hm[s2[i - ns1]]:
                count += 1
            if s2[i] in s1hm and s2[i] in s2hm and s2hm[s2[i]] == s1hm[s2[i]]:
                count -= 1
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1
            if s2[i] in s1hm and s2hm[s2[i]] == s1hm[s2[i]]:
                count += 1
        return count == len(s1hm)