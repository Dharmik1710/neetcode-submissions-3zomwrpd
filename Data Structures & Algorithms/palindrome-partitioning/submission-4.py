class Solution:

    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        
        def dfs(i: int, l: List[int]):
            if i == len(s):
                res.append(l.copy())
                return
            
            j = i
            while j < len(s):
                if isPalindrome(i, j):
                    l.append(s[i: j+1])
                    dfs(j+1, l)
                    l.pop()
                j+=1
            return
        
        dfs(0, [])        
        return res
    
                

