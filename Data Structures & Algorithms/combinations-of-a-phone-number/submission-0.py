class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        def dfs(i: int, l: List[str]) -> None:
            if i == len(digits):
                res.append("".join(l))
                return
            
            j = 0
            letters = d[digits[i]]
            while j < len(letters):
                l.append(letters[j])
                dfs(i+1, l)
                l.pop()
                j+=1
            return
        
        dfs(0, [])
        return res if digits else []
            