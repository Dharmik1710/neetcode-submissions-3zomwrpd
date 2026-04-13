class Solution:
    def search2D(self, arr: List[int], target: int) -> bool:
        print(arr)
        l, r = 0, len(arr) - 1
        while l<=r:
            m = (l+r)//2
            if arr[m] == target:
                return True
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t<=b:
            m = (t + b)//2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                return self.search2D(matrix[m], target)
            elif matrix[m][-1] > target:
                b = m-1
            else:
                t = m+1
        return False
