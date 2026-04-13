class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        ns, nt = len(s), len(t)
        l, r = 0, nt
        if ns < nt:
            return ""

        scount, tcount = {}, {}
        for i in range(nt):
            scount[s[i]] = scount.get(s[i], 0) + 1
            tcount[t[i]] = tcount.get(t[i], 0) + 1

        matches = 0
        for i in tcount:
            if i in scount and scount[i] >= tcount[i]:
                matches += 1    

        while r < ns:
            while r < ns and matches < len(tcount):
                scount[s[r]] = scount.get(s[r], 0) + 1 
                if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                    matches += 1
                print(r, matches)
                r += 1

            while l < r and matches == len(tcount):
                if s[l] in tcount:
                    if scount[s[l]] == tcount[s[l]]:
                        matches -= 1
                        if result == "" or r - l < len(result):
                            result = s[l:r]
                scount[s[l]] -= 1
                l += 1
        
        if matches == len(tcount):
            if result == "" or r - l < len(result):
                result = s[l:r]
        
        return result