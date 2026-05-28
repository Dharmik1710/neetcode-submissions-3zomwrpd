class Solution:

    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
               
        def dfs(i: int, l: List[int]):
            if i == len(s):
                res.append(l.copy())
                return
            
            j = i
            while j < len(s):
                if dp[i][j]:
                    l.append(s[i: j+1])
                    dfs(j+1, l)
                    l.pop()
                j+=1
            return
        
        dp, res = [], []
        i = 0
        while i < len(s):
            j = i
            tmp = [False]*len(s)
            while j < len(s):
                if isPalindrome(i, j):
                    tmp[j] = True
                j+=1
            dp.append(tmp.copy())
            i+=1
        
        dfs(0, [])        
        return res
    
                

