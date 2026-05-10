class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        stack = []

        def backtrack(i: int, k: int) -> None:

            if i == n:
                j = 0
                while j < k:
                    subset.append(')')
                    j+=1
                res.append("".join(subset))
                j=0
                while j < k:
                    subset.pop()
                    j+=1
                return
            
            if i < n:
                subset.append('(')
                backtrack(i+1, k+1)
                if k:
                    subset.pop()
                    subset.append(')')
                    backtrack(i, k-1) 
                subset.pop()          

        backtrack(0, 0)
        return res


